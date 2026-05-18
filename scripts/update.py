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

Read these official pages using the url_context tool:
{urls}

Write the **body** of the markdown page (no frontmatter, no top-level H1, no `# {name}` heading — we add those). You decide the structure, headings, tables, and column shapes — whatever best fits this provider's pricing. Some guidance:

- Include **every** model the provider publishes pricing for. Chat, reasoning, realtime / audio, image generation, video generation, speech (STT / TTS / translation), embeddings, moderation, fine-tuning base fees, anything else. Don't drop a model because it doesn't fit a column shape — give it its own table or section.
- Group models into `### <Category>` subsections under a top-level `## Models` heading. Pick category names that match what the provider actually publishes.
- Use GFM markdown tables. Choose columns that fit the modality (e.g. chat models want Input/Output $/MTok; speech models want $/min; image models want $/image or token rates per modality). Be exact — never round prices.
- For tiered pricing (e.g. ≤200K vs >200K context), emit one row per tier.
- Show model IDs in backticks, verbatim from the docs.
- Capabilities: short comma list (`vision, tools, reasoning`). Skip "text" — it's the default.
- End with a `## Notes` heading and 3–7 short bullets covering provider-level facts that matter for picking a model: batch discounts, prompt-caching mechanics, fine-tuning availability, free tiers, regional restrictions, deprecation policies.

Rules:
- Use only data visible at the URLs above. Do not pull from training data.
- USD only. No emojis, no marketing copy, no closing paragraph.
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


RETRYABLE_MARKERS = ("503", "429", "UNAVAILABLE", "RESOURCE_EXHAUSTED", "DEADLINE_EXCEEDED")
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
        body=body.strip(),
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
