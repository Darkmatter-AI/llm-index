# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.0.0",
# ]
# ///
"""Weekly updater for provider markdown pages.

The LLM does the heavy lifting. For each provider:

  1. Gemini reads the official pricing/models pages via the url_context
     tool and writes the full markdown body (categorized tables for
     chat / reasoning / realtime / image / video / speech / embeddings
     / other, plus a Notes section). We just wrap it with frontmatter,
     a nav strip, and the sources line.
  2. After all extractions, Gemini gets called once more with the run's
     token totals and the freshly-extracted providers/google.md, and
     produces a single COST line for the commit message.

Required env:
  GEMINI_API_KEY   API key for Google AI Studio.
  GEMINI_MODEL     Optional. Defaults to gemini-2.5-pro.

Usage:
  uv run scripts/update.py                # update all providers
  uv run scripts/update.py anthropic gpt  # update specific slugs
  uv run scripts/update.py --reflow       # re-wrap existing pages
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parent.parent
SOURCES_PATH = ROOT / "scripts" / "sources.json"
PROVIDERS_DIR = ROOT / "providers"
DEFAULT_MODEL = "gemini-3-flash-preview"

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

**Sources:** {sources_inline}  ·  **Updated:** `{timestamp}`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

{body}
"""

EXTRACT_PROMPT = """\
You are the editor of a public reference page for the AI provider **{name}** ({label}).
This page is consumed by AI coding agents and engineers picking a model. **Completeness and specificity are more important than brevity.** A reader must never have to click through to the provider's site to learn what a model supports.

## Sources

Read these official pages using the url_context tool:
{urls}

**Follow links when useful.** Provider sites usually have a top-level pricing/models index and a *per-model spec page* for each model (e.g. Google has `ai.google.dev/gemini-api/docs/models/<model-id>`, OpenAI has `platform.openai.com/docs/models/<model-id>`, Anthropic has per-model rows in the models overview). Read the index pages first; if you find a per-model spec page that has fields the index doesn't expose (modalities, context window, knowledge cutoff, feature matrix), fetch it too via the url_context tool. Stay under ~20 url_context fetches per call — if a provider has many models, prioritise the index plus the spec pages for the *latest 1–2 generations* and rely on the index for older/deprecated models.

## Output shape

Write only the **body** of the markdown page (no frontmatter, no top-level H1, no `# {name}` heading — we add those). Structure:

1. `## Models` — group models into `### <Category>` subsections (Chat / Reasoning / Realtime / Image / Video / Speech / Embeddings / Specialized / Deprecated, whatever the provider actually publishes). Use category names the provider uses when reasonable.
2. `## Notes` — 4–10 short bullets at the end covering provider-level facts (batch discount %, prompt-cache mechanics & TTL, free tier, regional/data-residency options, deprecation policy, rate-limit tiers, tool/billing extras).

## Mandatory per-model data — text/chat/reasoning models

For **every** chat, reasoning, realtime, audio-understanding, or vision model, the page MUST surface ALL of the following. Split across two tables per category if one table gets too wide — do not drop columns.

- **Model ID** — exact string in backticks, verbatim from the docs.
- **Aliases / snapshots** — every other ID the model is reachable by (e.g. dateless alias `claude-sonnet-4-6`, `-latest` suffixes, Bedrock IDs, Vertex IDs, dated snapshot pins like `-20251001`). One column or sub-list; do not silently drop any.
- **Inputs** — explicit comma list of accepted modalities: `text`, `image`, `audio`, `video`, `PDF`, `code`. Never write just "vision" — list every input modality the docs claim.
- **Outputs** — modalities the model can return: `text`, `audio`, `image`. Default is `text`; still write it.
- **Context window** — max input tokens, exact number (e.g. `1,048,576`).
- **Max output** — max output tokens per call, exact number (e.g. `65,536`). If a higher cap is available via a beta header or batch endpoint, note it in parentheses.
- **Knowledge cutoff** — month + year as stated in the docs (e.g. `Jan 2025`). If the docs distinguish *reliable knowledge cutoff* vs *training data cutoff*, list both. If not documented, write `—`.
- **Release stage** — `Stable`, `Preview`, `Experimental`, or `Deprecated`. For deprecated models, include the announced shutdown / retirement date.
- **Languages** — number of supported languages or named list, exactly as the docs state. Write `—` if not documented.
- **Capabilities** — explicit comma list pulled from the per-model "Supported features" matrix. Include every supported feature the docs name: `function calling`, `structured outputs`, `streaming`, `system instructions`, `caching` / `prompt caching`, `batch`, `code execution`, `file search`, `search grounding`, `URL context`, `thinking` / `extended thinking` / `adaptive thinking` / `reasoning`, `live API`, `web search`, `computer use`, `image generation`, `audio generation`, `fine-tuning`, `flex inference`, `priority inference`, `grounding with Google Maps`, `vision`, `multilingual`, etc. **Do not collapse this to `vision, tools`.** If the docs explicitly say a feature is *not* supported, you may add a short `Not: <feature>` qualifier.
- **Latency tier / SLA** — what service tiers the model supports (e.g. `Standard`, `Priority`, `Flex`, `Batch`, `Scale`) and the published comparative latency class if any (`Fastest` / `Fast` / `Moderate`).
- **Rate limits** — if the docs publish per-tier RPM/TPM caps for this model (e.g. Free / Tier 1 / Tier 2 / Tier 3 / Tier 4 / Tier 5, or Trial / Pay-as-you-go), include them. A compact sub-table like `Tier: RPM / TPM / RPD` is fine. If only an overall provider-wide limits page is published (not per model), summarise in `## Notes` instead and write `see Notes` here.
- **Pricing** — input $/MTok, cached-input $/MTok (if offered), output $/MTok. For tiered pricing (e.g. ≤200K vs >200K context, standard vs batch vs priority, regional multipliers), emit one row per tier and label the tier clearly. Never round; copy the exact decimal.

## Mandatory per-model data — other modalities

- **Image generation**: model ID, inputs (text / image / image+mask), output resolution(s), price per image *and* per token if both are billed, batch discount if any.
- **Video generation**: model ID, max duration, supported resolutions, price per second per resolution, audio-on/off pricing if separated.
- **Speech / TTS / STT / translation**: model ID, direction, supported languages count if stated, price per minute *and* per MTok if dual-billed.
- **Embeddings**: model ID, output dimensions (and whether Matryoshka/reducible), max input tokens, supported input modalities (text / image / audio / video / code), price per MTok per modality.
- **Moderation / fine-tuning / specialized (computer use, robotics, deep research, etc.)**: model ID, what it does in one phrase, all pricing components.

## Hard rules

- Include **every** model the provider lists with public pricing or spec details. Do **not** drop a model because it doesn't fit a column shape — give it its own table or row.
- Show model IDs in backticks, verbatim. Preserve dated suffixes (`-12-2025`, `-preview`, etc.).
- Use GFM markdown tables. Exact prices — never round. **Always leave a blank line between any heading (`###`, `####`) or bold label (`**Foo**`) and the table row that follows it** — kramdown (the renderer) collapses the table to plain text otherwise.
- Prefer `####` subheadings over bold labels when you need to subdivide a `###` section. Reserve bold labels for inline emphasis.
- USD only. No emojis. No marketing copy. No opening or closing paragraph.
- Use only data visible at the URLs (index + per-model pages). Do not pull from training data. If a field is not in the docs, write `—` (em-dash), do not guess.
- If every source URL is unreachable, output exactly: `## Models\\n\\n_Sources unreachable on {today}._\\n\\n## Notes\\n\\n_Sources unreachable on {today}._`
"""

COST_PROMPT = """\
You are the Gemini model `{model}` and you just ran an extraction job that produced one markdown page per AI provider. Compute the dollar cost of that job.

Inputs:
- Your model id: `{model}`
- Total prompt tokens (input) across all extraction calls: {total_in}
- Total candidate tokens (output) across all extraction calls: {total_out}
- Total cached input tokens: {total_cached}
- Number of extraction calls: {num_calls}
- The freshly-extracted Google/Gemini pricing page (your own provider) is below.

<gemini-page>
{gemini_md}
</gemini-page>

Find your model id in that page, pick the correct tier given an average call has roughly {avg_prompt} input tokens, and compute the cost. If any of the input was cached, bill that slice at the cached-input rate and the rest at the standard input rate. URL-context content is already counted in the prompt token total — do not add anything for it.

Output a single line, no other text, no markdown, no code fence:

COST: $X.XXXX (model: `{model}`, in: <N> tok @ $A/MTok, out: <N> tok @ $B/MTok, ...)

If your exact model id is not in the page, pick the closest match and prefix the dollar amount with `~`. Round to 4 decimal places.
"""


def normalize_body(body: str) -> str:
    """Insert a blank line between a heading or bold label and an immediately
    following GFM table row. kramdown (Jekyll's default renderer) needs the
    blank line or the whole block renders as paragraph text with literal pipes.
    """
    lines = body.splitlines()
    out: list[str] = []
    for i, line in enumerate(lines):
        out.append(line)
        if i + 1 >= len(lines):
            continue
        nxt = lines[i + 1]
        if not nxt.startswith("|"):
            continue
        stripped = line.strip()
        is_heading = stripped.startswith("#")
        is_bold_label = (
            stripped.startswith("**")
            and stripped.endswith("**")
            and len(stripped) > 4
        )
        if is_heading or is_bold_label:
            out.append("")
    return "\n".join(out)


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


def build_extract_prompt(provider: dict, today: str) -> str:
    return EXTRACT_PROMPT.format(
        name=provider["name"],
        label=provider["label"],
        urls="\n".join(f"- {u}" for u in provider["urls"]),
        today=today,
    )


def usage_of(response) -> tuple[int, int, int]:
    meta = getattr(response, "usage_metadata", None)
    if not meta:
        return 0, 0, 0
    return (
        getattr(meta, "prompt_token_count", 0) or 0,
        getattr(meta, "candidates_token_count", 0) or 0,
        getattr(meta, "cached_content_token_count", 0) or 0,
    )


RETRYABLE_MARKERS = (
    "503",
    "429",
    "UNAVAILABLE",
    "RESOURCE_EXHAUSTED",
    "DEADLINE_EXCEEDED",
    "INVALID_ARGUMENT",  # url_context occasionally 400s when many fetches are requested
    "Server disconnected",  # transient transport errors
    "ConnectError",
    "ReadTimeout",
)
RETRY_BACKOFF_SECONDS = (10, 30, 90)


def is_retryable(exc: BaseException) -> bool:
    return any(marker in str(exc) for marker in RETRYABLE_MARKERS)


def extract(
    client: genai.Client, model: str, provider: dict, today: str
) -> tuple[str, int, int, int]:
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
                contents=build_extract_prompt(provider, today),
                config=types.GenerateContentConfig(
                    tools=[types.Tool(url_context=types.UrlContext())],
                    temperature=0.1,
                ),
            )
            text = (response.text or "").strip()
            if not text:
                raise RuntimeError(f"empty response for {provider['slug']}")
            in_tok, out_tok, cached_tok = usage_of(response)
            return text, in_tok, out_tok, cached_tok
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            if not is_retryable(exc):
                raise
            print(f"  transient error: {str(exc)[:120]}", file=sys.stderr)
    raise last_err  # type: ignore[misc]


def write_page(provider: dict, body: str, timestamp: str, all_providers: dict) -> Path:
    label = provider.get("label", "")
    label_suffix = f" ({label})" if label and label != provider["name"] else ""
    page = PAGE_TEMPLATE.format(
        name=provider["name"],
        slug=provider["slug"],
        timestamp=timestamp,
        sources_yaml=render_sources_yaml(provider["urls"]),
        sources_inline=render_sources_inline(provider["urls"]),
        nav=render_nav(provider["slug"], all_providers),
        label_suffix=label_suffix,
        body=normalize_body(body.strip()),
    )
    out = PROVIDERS_DIR / f"{provider['slug']}.md"
    out.write_text(page)
    return out


def reflow(sources: dict) -> int:
    """Re-wrap existing provider markdown with the current TEMPLATE.

    Preserves the body (everything from the first `##` heading onward) and the
    existing `last_updated` timestamp. No Gemini calls.
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
        idx = existing.find("\n## ")
        if idx == -1:
            print(f"skip {slug}: no body found")
            skipped += 1
            continue
        body = existing[idx + 1 :].rstrip()
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


def estimate_cost(
    client: genai.Client,
    model: str,
    total_in: int,
    total_out: int,
    total_cached: int,
    num_calls: int,
) -> str:
    gemini_page = PROVIDERS_DIR / "google.md"
    if not gemini_page.exists():
        return f"COST: unavailable (google.md missing, model: `{model}`)"
    avg_prompt = (total_in // num_calls) if num_calls else 0
    prompt = COST_PROMPT.format(
        model=model,
        total_in=total_in,
        total_out=total_out,
        total_cached=total_cached,
        num_calls=num_calls,
        avg_prompt=avg_prompt,
        gemini_md=gemini_page.read_text(),
    )
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.0),
    )
    for line in (response.text or "").splitlines():
        c = line.strip()
        if c.startswith("COST:"):
            return c
    return f"COST: unavailable (no parseable line, model: `{model}`)"


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

    model = os.environ.get("GEMINI_MODEL") or DEFAULT_MODEL
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
            body, in_tok, out_tok, cached_tok = extract(client, model, provider, today)
            path = write_page(provider, body, timestamp, sources)
            total_in += in_tok
            total_out += out_tok
            total_cached += cached_tok
            num_calls += 1
            print(
                f"  wrote {path.relative_to(ROOT)}  (in:{in_tok} out:{out_tok}"
                + (f" cached:{cached_tok}" if cached_tok else "")
                + ")"
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
        try:
            cost_line = estimate_cost(client, model, total_in, total_out, total_cached, num_calls)
        except Exception as exc:  # noqa: BLE001
            cost_line = f"COST: unavailable ({exc}, model: `{model}`)"
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
