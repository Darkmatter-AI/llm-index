# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.0.0",
# ]
# ///
"""Daily updater for provider markdown pages.

Reads scripts/sources.json, asks Gemini to read each provider's official pricing/models
pages via the URL-context tool, and rewrites the corresponding providers/<slug>.md.
After extraction, asks the running Gemini model to estimate the dollar cost of the
run using its own freshly-extracted Google pricing table.

Required env:
  GEMINI_API_KEY   API key for Google AI Studio.
  GEMINI_MODEL     Optional. Defaults to gemini-2.5-pro.

Side effects:
  - Writes providers/<slug>.md for each target.
  - Prints `COST_ESTIMATE: ...` on stdout.
  - When run under GitHub Actions, appends `cost_estimate=<line>` to $GITHUB_OUTPUT.

Usage:
  uv run scripts/update.py                # update all providers
  uv run scripts/update.py anthropic gpt  # update specific slugs
"""

from __future__ import annotations

import json
import os
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

A single GitHub-flavored markdown table. Header (use this exact column order):

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |

One row per generally-available model. Conventions:
- **Model**: display name (e.g. `Claude Opus 4.7`)
- **ID**: API identifier in backticks (e.g. `` `claude-opus-4-7` ``), verbatim from docs
- **Context**: input window in tokens, abbreviated (`200K`, `1M`)
- **Max Out**: max output tokens, abbreviated, or `—` if not listed
- **Input / Output / Cached In**: USD per 1M tokens (e.g. `$3.00`). Use `—` when not offered.
- **Capabilities**: short comma list (`vision, tools, reasoning`). Omit obvious defaults like "text".
- **Cutoff**: knowledge cutoff `MMM YYYY` (e.g. `Jan 2025`) or `—`

Order rows newest/most-capable first. If a model has tiered pricing (e.g. ≤200K vs >200K context), use two rows with the same Model name and a parenthetical tier in the ID column (e.g. `` `claude-opus-4-7` (≤200K) ``).

## Notes

Three to seven one-line bullets covering provider-level facts that matter for picking a model: batch API discounts, prompt-caching mechanics, fine-tuning availability, free tiers, regional restrictions, deprecation policies. Plain bullets, no sub-bullets.

Rules:
- Use only data visible at the URLs above. Do not pull from training data.
- Keep numbers exact (`$1.25`, not "around a buck"). Currency is USD; the `$/MTok` is in the header so cells just contain the number (`$3.00`).
- No emojis. No marketing copy. No closing paragraph. No extra sections beyond `## Models` and `## Notes`.
- If every source URL is unreachable or empty, output exactly: `## Models\\n\\n_Sources unreachable on {today}._\\n\\n## Notes\\n\\n_Sources unreachable on {today}._`
"""

COST_PROMPT = """\
You are running as the Gemini model `{model}`. You just finished an extraction run that produced one markdown table per AI provider. Estimate the dollar cost of that run.

Inputs you have:
- Your model id: `{model}`
- Total prompt tokens consumed across all extraction calls (input): {total_in}
- Total candidate tokens produced across all extraction calls (output): {total_out}
- Number of extraction calls: {num_calls}
- The freshly-extracted Google/Gemini pricing table (your own provider):

<gemini-page>
{gemini_md}
</gemini-page>

Look up your model's row in that table, apply the Input and Output prices to the totals above, and pick the correct tier if the model has tiered pricing (assume per-call prompt size of roughly {avg_prompt} input tokens). The `prompt_tokens` count already includes content fetched by the url_context tool, so do not add anything for that.

Output a single line, no other text, no markdown, no code fence:

COST_ESTIMATE: $X.XXXX (model: `{model}`, in: {total_in} tok @ $A.AA/MTok, out: {total_out} tok @ $B.BB/MTok)

If your exact model id is not in the table, pick the closest match and prefix the dollar amount with `~`. Round to 4 decimal places.
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


def estimate_cost(
    client: genai.Client,
    model: str,
    total_in: int,
    total_out: int,
    num_calls: int,
) -> str:
    gemini_page = PROVIDERS_DIR / "google.md"
    if not gemini_page.exists():
        return f"COST_ESTIMATE: unavailable (google.md missing, model: `{model}`)"
    avg_prompt = (total_in // num_calls) if num_calls else 0
    prompt = COST_PROMPT.format(
        model=model,
        total_in=total_in,
        total_out=total_out,
        num_calls=num_calls,
        avg_prompt=avg_prompt,
        gemini_md=gemini_page.read_text(),
    )
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.0),
    )
    line = (response.text or "").strip().splitlines()
    for candidate in line:
        c = candidate.strip()
        if c.startswith("COST_ESTIMATE:"):
            return c
    return f"COST_ESTIMATE: unavailable (no parseable line, model: `{model}`)"


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
        try:
            estimate = estimate_cost(client, model, total_in, total_out, num_calls)
        except Exception as exc:  # noqa: BLE001
            estimate = f"COST_ESTIMATE: unavailable ({exc}, model: `{model}`)"
        print(estimate)
        emit_step_output("cost_estimate", estimate)
    else:
        emit_step_output("cost_estimate", "")

    if failures:
        print(f"\n{len(failures)} provider(s) failed: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
