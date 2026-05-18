# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.0.0",
#   "pydantic>=2.0",
# ]
# ///
"""Weekly updater for provider markdown pages.

Pipeline:

  1. For each provider in scripts/sources.json, call Gemini with the
     url_context tool to read official pricing/models pages.
  2. Gemini returns JSON validated against the pydantic schema below
     (ProviderData: models + provider-level notes).
  3. Save the structured data to data/<slug>.json.
  4. Render data/<slug>.json deterministically into providers/<slug>.md
     (categorized tables: Chat / Reasoning / Realtime / Image /
     Speech / Embedding / Other).

Cost is then computed by reading data/google.json (price-table for the
running GEMINI_MODEL) and multiplying against usage_metadata from
each call. No LLM call for the cost number.

Required env:
  GEMINI_API_KEY   API key for Google AI Studio.
  GEMINI_MODEL     Optional. Defaults to gemini-2.5-pro.

Side effects:
  - data/<slug>.json per provider (structured, authoritative)
  - providers/<slug>.md per provider (rendered for the site)
  - prints `COST: ...` on stdout, emits step output `cost_estimate`.

Usage:
  uv run scripts/update.py                # update all providers
  uv run scripts/update.py anthropic gpt  # update specific slugs
  uv run scripts/update.py --reflow       # re-render md from existing json
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from google import genai
from google.genai import types
from pydantic import BaseModel, ValidationError

ROOT = Path(__file__).resolve().parent.parent
SOURCES_PATH = ROOT / "scripts" / "sources.json"
PROVIDERS_DIR = ROOT / "providers"
DATA_DIR = ROOT / "data"
DEFAULT_MODEL = "gemini-2.5-pro"

# ---------------------------------------------------------------------------
# Schema (also serialized into the extraction prompt below)
# ---------------------------------------------------------------------------

Category = Literal[
    "chat",
    "reasoning",
    "realtime",
    "image",
    "speech",
    "video",
    "embedding",
    "moderation",
    "other",
]

PriceKind = Literal[
    "input",
    "output",
    "cached_input",
    "cache_write",
    "cache_read",
    "audio_input",
    "audio_output",
    "text_input",
    "text_output",
    "image_input",
    "image_output",
    "cached_audio_input",
    "cached_text_input",
    "cached_image_input",
]


class Price(BaseModel):
    kind: PriceKind
    amount: float
    unit: str = "1M tokens"  # "1M tokens" | "minute" | "image" | "1k characters" | "request"
    tier: str = ""
    note: str = ""


class Model(BaseModel):
    name: str
    id: str
    category: Category
    context_tokens: int | None = None
    max_output_tokens: int | None = None
    dimensions: int | None = None
    capabilities: list[str] = []
    cutoff: str | None = None
    prices: list[Price] = []
    notes: str = ""


class ProviderData(BaseModel):
    notes: list[str] = []
    models: list[Model] = []


class ProviderFile(BaseModel):
    provider: str
    slug: str
    label: str = ""
    last_updated: str
    sources: list[str]
    notes: list[str] = []
    models: list[Model] = []


# ---------------------------------------------------------------------------
# Extraction prompt
# ---------------------------------------------------------------------------

PROMPT = """\
You are populating a public reference dataset for the AI provider **{name}** ({label}).

Read these official pages with the url_context tool and extract every model the provider currently lists pricing for:
{urls}

Return ONLY a single raw JSON object as your entire response — no `\`\`\`json` fence, no `\`\`\`` fence, no prose before or after, no commentary, no explanation. The very first character of your response must be `{{` and the very last must be `}}`. The object must match this exact shape:

{{
  "notes": ["...3-7 short provider-level facts (batch discounts, fine-tuning, prompt-caching mechanics, free tiers, regional restrictions, deprecation policies)..."],
  "models": [
    {{
      "name": "Display name",
      "id": "exact-api-id-verbatim",
      "category": "chat" | "reasoning" | "realtime" | "image" | "speech" | "video" | "embedding" | "moderation" | "other",
      "context_tokens": 200000 | null,
      "max_output_tokens": 64000 | null,
      "dimensions": 3072 | null,
      "capabilities": ["vision", "tools", "reasoning", "audio", "..."],
      "cutoff": "Jan 2025" | null,
      "prices": [
        {{
          "kind": "input" | "output" | "cached_input" | "cache_write" | "cache_read" | "audio_input" | "audio_output" | "text_input" | "text_output" | "image_input" | "image_output" | "cached_audio_input" | "cached_text_input" | "cached_image_input",
          "amount": 1.25,
          "unit": "1M tokens" | "minute" | "image" | "1k characters" | "request",
          "tier": "" | "≤200K" | ">200K" | "...whatever the provider uses...",
          "note": ""
        }}
      ],
      "notes": ""
    }}
  ]
}}

Rules:
- Use only data visible at the URLs above. Do not pull from training data.
- Include every generally-available model. **Do not drop any model the provider publishes pricing for** — chat, reasoning, realtime / audio, image gen, speech (STT/TTS/translation), video, embeddings, moderation, fine-tuning base.
- Pick the closest `category` for each model.
- For tiered pricing (e.g. ≤200K vs >200K context), emit one Price entry per tier with `tier` set.
- For multi-modal pricing (e.g. realtime models with audio + text + image input rates), emit one Price entry per modality using the typed `kind`s above.
- For per-minute / per-image pricing, set `unit` accordingly (`"minute"`, `"image"`, `"1k characters"`).
- Use `cache_write` / `cache_read` only when the provider separates prompt-caching into a write fee + read fee (Anthropic-style). Otherwise use `cached_input` for the single cached-token rate.
- Keep numbers exact. Currency is USD.
- `capabilities`: short list, omit "text" (it's the default).
- Order `models` newest/most-capable first.
- If every source URL is unreachable, return `{{"notes": ["Sources unreachable on {today}."], "models": []}}`.
"""


# ---------------------------------------------------------------------------
# Rendering: data → markdown
# ---------------------------------------------------------------------------

PAGE_TEMPLATE = """\
---
provider: {name}
slug: {slug}
last_updated: {timestamp}
sources:
{sources_yaml}
---

[← Home](../) · {nav}

# {name}{label_suffix}

**Sources:** {sources_inline}  ·  **Updated:** `{timestamp}`  ·  [JSON](../data/{slug}.json)

{body}
"""


def fmt_tokens(n: int | None) -> str:
    if not n:
        return "—"
    if n >= 1_000_000:
        return f"{n // 1_000_000}M"
    if n >= 1_000:
        return f"{n // 1_000}K"
    return str(n)


def fmt_amount(amount: float | None) -> str:
    if amount is None:
        return "—"
    return f"${amount:g}"


def caps_str(caps: list[str]) -> str:
    return ", ".join(caps) if caps else "—"


def price_lookup(model: Model, kind: PriceKind, tier: str = "") -> Price | None:
    for p in model.prices:
        if p.kind == kind and p.tier == tier:
            return p
    if tier:
        return None
    # Allow tier=="" to match any single-tier price of that kind
    for p in model.prices:
        if p.kind == kind:
            return p
    return None


def tiers_of(model: Model, kind: PriceKind = "input") -> list[str]:
    seen: list[str] = []
    for p in model.prices:
        if p.kind == kind and p.tier not in seen:
            seen.append(p.tier)
    return seen or [""]


def _table(header: list[str], rows: list[list[str]]) -> str:
    sep = ["---"] * len(header)
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(sep) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_chat_table(models: list[Model]) -> str:
    header = [
        "Model",
        "ID",
        "Context",
        "Max Out",
        "Input $/MTok",
        "Output $/MTok",
        "Cached In $/MTok",
        "Capabilities",
        "Cutoff",
    ]
    rows: list[list[str]] = []
    for m in models:
        for tier in tiers_of(m):
            ip = price_lookup(m, "input", tier)
            op = price_lookup(m, "output", tier)
            cp = price_lookup(m, "cached_input", tier) or price_lookup(m, "cache_read", tier)
            id_label = f"`{m.id}`" + (f" ({tier})" if tier else "")
            rows.append([
                m.name,
                id_label,
                fmt_tokens(m.context_tokens),
                fmt_tokens(m.max_output_tokens),
                fmt_amount(ip.amount if ip else None),
                fmt_amount(op.amount if op else None),
                fmt_amount(cp.amount if cp else None),
                caps_str(m.capabilities),
                m.cutoff or "—",
            ])
    return _table(header, rows)


def render_realtime_table(models: list[Model]) -> str:
    header = [
        "Model",
        "ID",
        "Audio In $/MTok",
        "Audio Out $/MTok",
        "Text In $/MTok",
        "Text Out $/MTok",
        "Cached In $/MTok",
        "Notes",
    ]
    rows: list[list[str]] = []
    for m in models:
        ai = price_lookup(m, "audio_input")
        ao = price_lookup(m, "audio_output")
        ti = price_lookup(m, "text_input") or price_lookup(m, "input")
        to = price_lookup(m, "text_output") or price_lookup(m, "output")
        cached = (
            price_lookup(m, "cached_audio_input")
            or price_lookup(m, "cached_text_input")
            or price_lookup(m, "cached_input")
        )
        rows.append([
            m.name,
            f"`{m.id}`",
            fmt_amount(ai.amount if ai else None),
            fmt_amount(ao.amount if ao else None),
            fmt_amount(ti.amount if ti else None),
            fmt_amount(to.amount if to else None),
            fmt_amount(cached.amount if cached else None),
            m.notes or "—",
        ])
    return _table(header, rows)


def render_image_table(models: list[Model]) -> str:
    header = ["Model", "ID", "Text In $/MTok", "Image In $/MTok", "Image Out", "Unit", "Notes"]
    rows: list[list[str]] = []
    for m in models:
        ti = price_lookup(m, "text_input") or price_lookup(m, "input")
        ii = price_lookup(m, "image_input")
        io = price_lookup(m, "image_output") or price_lookup(m, "output")
        unit = (io.unit if io else (ii.unit if ii else (ti.unit if ti else "1M tokens")))
        rows.append([
            m.name,
            f"`{m.id}`",
            fmt_amount(ti.amount if ti else None),
            fmt_amount(ii.amount if ii else None),
            fmt_amount(io.amount if io else None),
            f"$/{unit}" if unit != "1M tokens" else "$/MTok",
            m.notes or "—",
        ])
    return _table(header, rows)


def render_speech_table(models: list[Model]) -> str:
    header = ["Model", "ID", "Input", "Output", "Unit", "Notes"]
    rows: list[list[str]] = []
    for m in models:
        ip = price_lookup(m, "input")
        op = price_lookup(m, "output")
        unit = (ip.unit if ip else (op.unit if op else "1M tokens"))
        rows.append([
            m.name,
            f"`{m.id}`",
            fmt_amount(ip.amount if ip else None),
            fmt_amount(op.amount if op else None),
            f"$/{unit}" if unit != "1M tokens" else "$/MTok",
            m.notes or "—",
        ])
    return _table(header, rows)


def render_embedding_table(models: list[Model]) -> str:
    header = ["Model", "ID", "Context", "Dimensions", "Input $/MTok", "Notes"]
    rows: list[list[str]] = []
    for m in models:
        ip = price_lookup(m, "input")
        rows.append([
            m.name,
            f"`{m.id}`",
            fmt_tokens(m.context_tokens),
            str(m.dimensions) if m.dimensions else "—",
            fmt_amount(ip.amount if ip else None),
            m.notes or "—",
        ])
    return _table(header, rows)


def render_other_table(models: list[Model]) -> str:
    header = ["Model", "ID", "Pricing", "Notes"]
    rows: list[list[str]] = []
    for m in models:
        pricing_parts: list[str] = []
        for p in m.prices:
            tag = p.kind.replace("_", " ")
            tier_part = f" ({p.tier})" if p.tier else ""
            unit_part = f"/{p.unit}" if p.unit != "1M tokens" else "/MTok"
            pricing_parts.append(f"{tag}: ${p.amount:g}{unit_part}{tier_part}")
        rows.append([
            m.name,
            f"`{m.id}`",
            "; ".join(pricing_parts) or "—",
            m.notes or "—",
        ])
    return _table(header, rows)


CATEGORY_RENDERERS: list[tuple[str, Category, callable]] = [
    ("Chat / completion", "chat", render_chat_table),
    ("Reasoning", "reasoning", render_chat_table),
    ("Realtime / audio", "realtime", render_realtime_table),
    ("Image generation", "image", render_image_table),
    ("Video generation", "video", render_other_table),
    ("Speech — transcription / TTS / translation", "speech", render_speech_table),
    ("Embeddings / reranking / moderation", "embedding", render_embedding_table),
    ("Moderation", "moderation", render_other_table),
    ("Other", "other", render_other_table),
]


def render_body(file: ProviderFile) -> str:
    parts: list[str] = ["## Models", ""]
    rendered_any = False
    for heading, category, renderer in CATEGORY_RENDERERS:
        models = [m for m in file.models if m.category == category]
        if not models:
            continue
        rendered_any = True
        parts.append(f"### {heading}")
        parts.append("")
        parts.append(renderer(models))
        parts.append("")

    if not rendered_any:
        parts.append("_No models extracted._")
        parts.append("")

    parts.append("## Notes")
    parts.append("")
    if file.notes:
        for note in file.notes:
            parts.append(f"- {note}")
    else:
        parts.append("_No provider notes extracted._")
    parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Page wrappers
# ---------------------------------------------------------------------------


def render_sources_yaml(urls: list[str]) -> str:
    return "\n".join(f"  - {u}" for u in urls)


def render_sources_inline(urls: list[str]) -> str:
    parts = []
    for u in urls:
        display = u.replace("https://", "").replace("http://", "").rstrip("/")
        parts.append(f"[{display}]({u})")
    return ", ".join(parts)


def render_nav(current_slug: str, all_providers: dict) -> str:
    parts = []
    for slug, provider in all_providers.items():
        label = provider["name"]
        if slug == current_slug:
            parts.append(f"**{label}**")
        else:
            parts.append(f"[{label}]({slug}.md)")
    return " · ".join(parts)


def build_page(file: ProviderFile, all_providers: dict) -> str:
    label = file.label
    label_suffix = f" ({label})" if label and label != file.provider else ""
    body = render_body(file)
    return PAGE_TEMPLATE.format(
        name=file.provider,
        slug=file.slug,
        timestamp=file.last_updated,
        sources_yaml=render_sources_yaml(file.sources),
        sources_inline=render_sources_inline(file.sources),
        nav=render_nav(file.slug, all_providers),
        label_suffix=label_suffix,
        body=body,
    )


# ---------------------------------------------------------------------------
# Gemini call + retry
# ---------------------------------------------------------------------------


def usage_of(response) -> tuple[int, int, int]:
    """Returns (prompt_tokens, candidates_tokens, cached_tokens).

    `cached_tokens` is the slice of `prompt_tokens` Gemini served from its
    prompt cache (billed at the cached rate); it is a subset of prompt_tokens.
    """
    meta = getattr(response, "usage_metadata", None)
    if not meta:
        return 0, 0, 0
    return (
        getattr(meta, "prompt_token_count", 0) or 0,
        getattr(meta, "candidates_token_count", 0) or 0,
        getattr(meta, "cached_content_token_count", 0) or 0,
    )


RETRYABLE_MARKERS = ("503", "429", "UNAVAILABLE", "RESOURCE_EXHAUSTED", "DEADLINE_EXCEEDED")
RETRY_BACKOFF_SECONDS = (10, 30, 90)


def is_retryable(exc: BaseException) -> bool:
    msg = str(exc)
    return any(marker in msg for marker in RETRYABLE_MARKERS)


def build_prompt(provider: dict, today: str) -> str:
    return PROMPT.format(
        name=provider["name"],
        label=provider["label"],
        urls="\n".join(f"- {u}" for u in provider["urls"]),
        today=today,
    )


def parse_json_lenient(text: str) -> dict:
    """Parse JSON from Gemini text output, tolerating markdown code fences."""
    s = text.strip()
    # Strip ``` / ```json fences if present
    if s.startswith("```"):
        s = s.split("\n", 1)[1] if "\n" in s else s[3:]
        if s.endswith("```"):
            s = s[: -3]
        s = s.strip()
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    start, end = s.find("{"), s.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(s[start : end + 1])
    raise RuntimeError(f"could not parse JSON; head: {text[:200]!r}")


def extract(
    client: genai.Client, model: str, provider: dict, today: str
) -> tuple[ProviderData, int, int, int]:
    last_err: BaseException | None = None
    for attempt, wait in enumerate([0, *RETRY_BACKOFF_SECONDS]):
        if wait:
            print(
                f"  retrying in {wait}s "
                f"(attempt {attempt + 1}/{len(RETRY_BACKOFF_SECONDS) + 1})"
            )
            time.sleep(wait)
        try:
            response = client.models.generate_content(
                model=model,
                contents=build_prompt(provider, today),
                # Note: response_mime_type="application/json" can't be combined
                # with the url_context tool ("Tool use with a response mime
                # type: 'application/json' is unsupported"). The prompt itself
                # demands JSON and we parse + validate in Python below.
                config=types.GenerateContentConfig(
                    tools=[types.Tool(url_context=types.UrlContext())],
                    temperature=0.1,
                ),
            )
            text = (response.text or "").strip()
            if not text:
                raise RuntimeError(f"empty response for {provider['slug']}")
            raw = parse_json_lenient(text)
            try:
                data = ProviderData.model_validate(raw)
            except ValidationError as ve:
                raise RuntimeError(f"schema validation failed: {ve}") from ve
            in_tok, out_tok, cached_tok = usage_of(response)
            return data, in_tok, out_tok, cached_tok
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            if not is_retryable(exc):
                raise
            print(f"  transient error: {str(exc)[:120]}", file=sys.stderr)
    raise last_err  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Disk I/O: JSON + rendered markdown
# ---------------------------------------------------------------------------


def write_provider(file: ProviderFile, all_providers: dict) -> tuple[Path, Path]:
    DATA_DIR.mkdir(exist_ok=True)
    PROVIDERS_DIR.mkdir(exist_ok=True)
    data_path = DATA_DIR / f"{file.slug}.json"
    md_path = PROVIDERS_DIR / f"{file.slug}.md"
    data_path.write_text(
        json.dumps(file.model_dump(), indent=2, ensure_ascii=False, sort_keys=False)
        + "\n"
    )
    md_path.write_text(build_page(file, all_providers))
    return data_path, md_path


def load_provider_file(slug: str) -> ProviderFile | None:
    path = DATA_DIR / f"{slug}.json"
    if not path.exists():
        return None
    return ProviderFile.model_validate_json(path.read_text())


# ---------------------------------------------------------------------------
# Reflow: re-render markdown from existing JSON, no Gemini calls
# ---------------------------------------------------------------------------


def reflow(sources: dict) -> int:
    reflowed = 0
    skipped = 0
    for slug in sources:
        file = load_provider_file(slug)
        if file is None:
            print(f"skip {slug}: no data/{slug}.json yet")
            skipped += 1
            continue
        write_provider(file, sources)
        print(f"reflowed providers/{slug}.md from data/{slug}.json")
        reflowed += 1
    print(f"\n{reflowed} reflowed, {skipped} skipped")
    return 0 if reflowed else 1


# ---------------------------------------------------------------------------
# Cost: deterministic, reads data/google.json
# ---------------------------------------------------------------------------


def find_gemini_prices(
    model_id: str, avg_input_tokens: int
) -> tuple[float, float, float | None, str] | None:
    """Returns (input, output, cached_input, tier) for `model_id` from data/google.json."""
    file = load_provider_file("google")
    if file is None:
        return None
    for m in file.models:
        if m.id != model_id:
            continue
        tiers = tiers_of(m)
        chosen = tiers[0]
        if len(tiers) > 1:
            for t in tiers:
                tt = t.replace(" ", "")
                if ("≤" in tt or "<" in tt) and avg_input_tokens <= 200_000:
                    chosen = t
                    break
                if (">" in tt and "≤" not in tt) and avg_input_tokens > 200_000:
                    chosen = t
                    break
        ip = price_lookup(m, "input", chosen)
        op = price_lookup(m, "output", chosen)
        cp = price_lookup(m, "cached_input", chosen) or price_lookup(m, "cache_read", chosen)
        if not ip or not op:
            return None
        return ip.amount, op.amount, (cp.amount if cp else None), chosen
    return None


def compute_cost_line(
    model: str,
    total_in: int,
    total_out: int,
    total_cached: int,
    num_calls: int,
) -> str:
    avg_input = (total_in // num_calls) if num_calls else 0
    found = find_gemini_prices(model, avg_input)
    if not found:
        return (
            f"COST: unavailable (model `{model}` not found in data/google.json; "
            f"tokens — in:{total_in} out:{total_out} cached:{total_cached})"
        )
    in_price, out_price, cached_price, tier = found
    billable_in = max(total_in - total_cached, 0)
    cached_cost = (total_cached * (cached_price or 0)) / 1_000_000
    cost = (billable_in * in_price + total_out * out_price) / 1_000_000 + cached_cost
    tier_part = f", tier: {tier}" if tier else ""
    cached_part = (
        f", cached: {total_cached:,} tok @ ${cached_price:g}/MTok"
        if total_cached and cached_price is not None
        else ""
    )
    return (
        f"COST: ${cost:.4f} (model: `{model}`, "
        f"in: {billable_in:,} tok @ ${in_price:g}/MTok, "
        f"out: {total_out:,} tok @ ${out_price:g}/MTok"
        f"{cached_part}{tier_part})"
    )


# ---------------------------------------------------------------------------
# Step output (GitHub Actions)
# ---------------------------------------------------------------------------


def emit_step_output(key: str, value: str) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{key}<<EOF_LLM_INDEX\n{value}\nEOF_LLM_INDEX\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    sources = json.loads(SOURCES_PATH.read_text())

    if "--reflow" in sys.argv[1:]:
        return reflow(sources)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY is not set", file=sys.stderr)
        return 2

    model = os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)
    requested = sys.argv[1:]
    if requested:
        unknown = [s for s in requested if s not in sources]
        if unknown:
            print(f"ERROR: unknown provider slug(s): {unknown}", file=sys.stderr)
            return 2
        targets = {s: sources[s] for s in requested}
    else:
        targets = sources

    client = genai.Client(api_key=api_key)
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    today = now.strftime("%Y-%m-%d")

    failures: list[str] = []
    total_in = 0
    total_out = 0
    total_cached = 0
    num_calls = 0
    for slug, provider in targets.items():
        print(f"→ {slug} ({provider['name']})")
        try:
            data, in_tok, out_tok, cached_tok = extract(client, model, provider, today)
            file = ProviderFile(
                provider=provider["name"],
                slug=slug,
                label=provider.get("label", ""),
                last_updated=timestamp,
                sources=provider["urls"],
                notes=data.notes,
                models=data.models,
            )
            data_path, md_path = write_provider(file, sources)
            total_in += in_tok
            total_out += out_tok
            total_cached += cached_tok
            num_calls += 1
            print(
                f"  wrote {data_path.relative_to(ROOT)} + "
                f"{md_path.relative_to(ROOT)}  (in:{in_tok} out:{out_tok}"
                + (f" cached:{cached_tok}" if cached_tok else "")
                + f"  models:{len(data.models)})"
            )
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}", file=sys.stderr)
            failures.append(slug)

    if num_calls:
        print(
            f"\nTotal tokens — in: {total_in:,}  out: {total_out:,}"
            + (f"  cached: {total_cached:,}" if total_cached else "")
            + f"  calls: {num_calls}"
        )
        cost_line = compute_cost_line(model, total_in, total_out, total_cached, num_calls)
        print(cost_line)
        emit_step_output("cost_estimate", cost_line)
    else:
        emit_step_output("cost_estimate", "")

    if failures:
        print(f"\n{len(failures)} provider(s) failed: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
