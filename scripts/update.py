# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.0.0",
# ]
# ///
"""Daily updater for provider markdown pages.

Reads scripts/sources.json, asks Gemini to read each provider's official pricing/models
pages via the URL-context tool, and rewrites the corresponding providers/<slug>.md.
After extraction, computes the run's exact dollar cost by:

  1. Summing prompt_token_count + candidates_token_count from each call's
     usage_metadata (this is what Gemini bills against; URL-context content
     is already folded into prompt_token_count).
  2. Parsing the freshly-written providers/google.md for the input/output
     $/MTok of the running GEMINI_MODEL (correct tier picked from average
     prompt size).
  3. Multiplying. No LLM call, no estimation.

Required env:
  GEMINI_API_KEY   API key for Google AI Studio.
  GEMINI_MODEL     Optional. Defaults to gemini-2.5-pro.

Side effects:
  - Writes providers/<slug>.md for each target.
  - Prints `COST: ...` on stdout.
  - When run under GitHub Actions, appends `cost_estimate=<line>` to $GITHUB_OUTPUT.

Usage:
  uv run scripts/update.py                # update all providers
  uv run scripts/update.py anthropic gpt  # update specific slugs
  uv run scripts/update.py --reflow       # rewrap existing pages (no Gemini calls)
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parent.parent
SOURCES_PATH = ROOT / "scripts" / "sources.json"
PROVIDERS_DIR = ROOT / "providers"
DEFAULT_MODEL = "gemini-2.5-pro"

TEMPLATE = """\
---
provider: {name}
slug: {slug}
last_updated: {timestamp}
sources:
{sources_yaml}
---

[← Home](../) · {nav}

# {name}{label_suffix}

**Sources:** {sources_inline}  ·  **Updated:** `{timestamp}`

{body}
"""

PROMPT = """\
You are populating a public reference page for the AI provider **{name}** ({label}).

Read these official pages using the url_context tool:
{urls}

Extract the **current** publicly listed information and produce a markdown **body** (no frontmatter, no top-level H1) with this exact structure:

## Models

Group models into categorized tables under `### <Category>` subheadings. **Include every model the provider publishes pricing for** — chat, realtime, audio, image, speech, embeddings, moderation, fine-tuning base prices, etc. Omit a category only when the provider has zero models in it.

Use these category headings and column shapes:

**`### Chat / completion`** — text-in, text-out language models.
Columns: `| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |`

**`### Reasoning`** — only if the provider lists reasoning models as a distinct line item with their own prices (otherwise put them in Chat / completion with `reasoning` in Capabilities).
Same columns as Chat / completion.

**`### Realtime / audio`** — speech-to-speech / live audio models priced per token across modalities.
Columns: `| Model | ID | Audio In $/MTok | Audio Out $/MTok | Text In $/MTok | Text Out $/MTok | Cached In $/MTok | Notes |`

**`### Image generation`** — text-to-image or image-edit models.
Columns: `| Model | ID | Text In $/MTok | Image In $/MTok | Image Out $/MTok or $/image | Notes |`

**`### Speech — transcription / TTS / translation`** — STT / TTS models, often priced per minute.
Columns: `| Model | ID | Input | Output | Unit | Notes |` (Unit values like `$/min`, `$/MTok`, `$/1k chars`)

**`### Embeddings / reranking / moderation`** — vector and classifier models.
Columns: `| Model | ID | Context | Dimensions | Input $/MTok | Notes |`

**`### Other`** — anything that doesn't fit (search APIs, code-interp, batch-only models, etc.).
Columns: `| Model | ID | Pricing | Notes |`

General row conventions:
- **Model**: display name (e.g. `Claude Opus 4.7`, `gpt-realtime-2`)
- **ID**: API identifier in backticks, verbatim from docs (e.g. `` `claude-opus-4-7` ``)
- **Context / Max Out**: abbreviated tokens (`200K`, `1M`), or `—` if not listed
- All `$/MTok` cells: USD per 1M tokens, just the number with `$` prefix (e.g. `$3.00`). Use `—` when not offered.
- **Capabilities**: short comma list (`vision, tools, reasoning`). Omit "text" — it's the default.
- **Cutoff**: `MMM YYYY` (e.g. `Jan 2025`) or `—`
- Tiered pricing: emit one row per tier with the same Model name and a parenthetical tier in the ID column (e.g. `` `claude-opus-4-7` (≤200K) ``).

Order rows newest/most-capable first within each table.

## Notes

Three to seven one-line bullets covering provider-level facts that matter for picking a model: batch API discounts, prompt-caching mechanics, fine-tuning availability, free tiers, regional restrictions, deprecation policies. Plain bullets, no sub-bullets.

Rules:
- Use only data visible at the URLs above. Do not pull from training data.
- **Do not drop any model the provider publishes pricing for.** If a model doesn't fit a column shape, pick the closest category and put the missing detail in Notes.
- Keep numbers exact (`$1.25`, not "around a buck"). Currency is USD.
- No emojis. No marketing copy. No closing paragraph. No top-level sections beyond `## Models` and `## Notes`.
- If every source URL is unreachable or empty, output exactly: `## Models\\n\\n_Sources unreachable on {today}._\\n\\n## Notes\\n\\n_Sources unreachable on {today}._`
"""



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


def build_prompt(provider: dict, today: str) -> str:
    return PROMPT.format(
        name=provider["name"],
        label=provider["label"],
        urls="\n".join(f"- {u}" for u in provider["urls"]),
        today=today,
    )


def usage_of(response) -> tuple[int, int]:
    meta = getattr(response, "usage_metadata", None)
    if not meta:
        return 0, 0
    return (
        getattr(meta, "prompt_token_count", 0) or 0,
        getattr(meta, "candidates_token_count", 0) or 0,
    )


def extract(
    client: genai.Client, model: str, provider: dict, today: str
) -> tuple[str, int, int]:
    response = client.models.generate_content(
        model=model,
        contents=build_prompt(provider, today),
        config=types.GenerateContentConfig(
            tools=[types.Tool(url_context=types.UrlContext())],
            temperature=0.1,
        ),
    )
    text = (response.text or "").strip()
    if not text:
        raise RuntimeError(f"empty response for {provider['slug']}")
    in_tok, out_tok = usage_of(response)
    return text, in_tok, out_tok


def write_page(
    provider: dict, body: str, timestamp: str, all_providers: dict
) -> Path:
    label = provider.get("label", "")
    label_suffix = f" ({label})" if label and label != provider["name"] else ""
    page = TEMPLATE.format(
        name=provider["name"],
        slug=provider["slug"],
        timestamp=timestamp,
        sources_yaml=render_sources_yaml(provider["urls"]),
        sources_inline=render_sources_inline(provider["urls"]),
        nav=render_nav(provider["slug"], all_providers),
        label_suffix=label_suffix,
        body=body.strip(),
    )
    out = PROVIDERS_DIR / f"{provider['slug']}.md"
    out.write_text(page)
    return out


def reflow(sources: dict) -> int:
    """Re-wrap existing provider markdown with the current TEMPLATE.

    Preserves the body (everything from `## Models` onward) and the existing
    `last_updated` timestamp. Does not call Gemini — useful after template
    changes.
    """
    reflowed = 0
    skipped = 0
    for slug, provider in sources.items():
        path = PROVIDERS_DIR / f"{slug}.md"
        if not path.exists():
            print(f"skip {slug}: no file")
            skipped += 1
            continue
        existing = path.read_text()
        idx = existing.find("## Models")
        if idx == -1:
            print(f"skip {slug}: no '## Models' section")
            skipped += 1
            continue
        body = existing[idx:].rstrip()
        timestamp = "pending-first-run"
        for line in existing.splitlines():
            if line.startswith("last_updated:"):
                timestamp = line.split(":", 1)[1].strip()
                break
        write_page(provider, body, timestamp, sources)
        print(f"reflowed providers/{slug}.md")
        reflowed += 1
    print(f"\n{reflowed} reflowed, {skipped} skipped")
    return 0


PRICE_RE = re.compile(r"\$([\d,]+\.?\d*)")


def find_model_prices(
    google_md: str, model_id: str, avg_input_tokens: int
) -> tuple[float, float, str] | None:
    """Find input/output $/MTok for `model_id` in the Gemini provider page.

    Returns (input_per_mtok, output_per_mtok, tier_label) or None if not found.
    Handles tiered pricing by picking the row matching `avg_input_tokens`.
    """
    matches: list[tuple[list[str], str]] = []
    for line in google_md.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        if f"`{model_id}`" not in stripped:
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        id_cell = cells[1] if len(cells) > 1 else ""
        tier_match = re.search(r"\(([^)]+)\)", id_cell)
        tier = tier_match.group(1) if tier_match else ""
        matches.append((cells, tier))

    if not matches:
        return None

    chosen_cells, chosen_tier = matches[0]
    if len(matches) > 1:
        for cells, tier in matches:
            if not tier:
                continue
            t = tier.replace(" ", "")
            if ("≤" in t or "<" in t) and avg_input_tokens <= 200_000:
                chosen_cells, chosen_tier = cells, tier
                break
            if (">" in t and "≤" not in t) and avg_input_tokens > 200_000:
                chosen_cells, chosen_tier = cells, tier
                break

    prices: list[float] = []
    for cell in chosen_cells:
        m = PRICE_RE.fullmatch(cell)
        if m:
            prices.append(float(m.group(1).replace(",", "")))
    if len(prices) < 2:
        return None
    return prices[0], prices[1], chosen_tier


def compute_cost_line(
    model: str, total_in: int, total_out: int, num_calls: int
) -> str:
    gemini_page = PROVIDERS_DIR / "google.md"
    if not gemini_page.exists():
        return f"COST: unavailable (google.md missing, model: `{model}`)"
    avg_input = (total_in // num_calls) if num_calls else 0
    found = find_model_prices(gemini_page.read_text(), model, avg_input)
    if not found:
        return (
            f"COST: unavailable (model `{model}` not found in google.md; "
            f"tokens — in:{total_in} out:{total_out})"
        )
    in_price, out_price, tier = found
    cost = (total_in * in_price + total_out * out_price) / 1_000_000
    tier_part = f", tier: {tier}" if tier else ""
    return (
        f"COST: ${cost:.4f} (model: `{model}`, "
        f"in: {total_in:,} tok @ ${in_price:g}/MTok, "
        f"out: {total_out:,} tok @ ${out_price:g}/MTok{tier_part})"
    )


def emit_step_output(key: str, value: str) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{key}<<EOF_LLM_INDEX\n{value}\nEOF_LLM_INDEX\n")


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
    num_calls = 0
    for slug, provider in targets.items():
        print(f"→ {slug} ({provider['name']})")
        try:
            body, in_tok, out_tok = extract(client, model, provider, today)
            path = write_page(provider, body, timestamp, sources)
            total_in += in_tok
            total_out += out_tok
            num_calls += 1
            print(f"  wrote {path.relative_to(ROOT)}  (in:{in_tok} out:{out_tok})")
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}", file=sys.stderr)
            failures.append(slug)

    if num_calls:
        print(f"\nTotal tokens — in: {total_in:,}  out: {total_out:,}  calls: {num_calls}")
        cost_line = compute_cost_line(model, total_in, total_out, num_calls)
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
