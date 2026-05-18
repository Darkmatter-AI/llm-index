# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.0.0",
# ]
# ///
"""Daily updater for provider markdown pages.

Reads scripts/sources.json, asks Gemini to read each provider's official pricing/models
pages via the URL-context tool, and rewrites the corresponding providers/<slug>.md.

Required env:
  GEMINI_API_KEY   API key for Google AI Studio.
  GEMINI_MODEL     Optional. Defaults to gemini-2.5-pro.

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

# {name}{label_suffix}

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

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


def render_sources_yaml(urls: list[str]) -> str:
    return "\n".join(f"  - {u}" for u in urls)


def build_prompt(provider: dict, today: str) -> str:
    return PROMPT.format(
        name=provider["name"],
        label=provider["label"],
        urls="\n".join(f"- {u}" for u in provider["urls"]),
        today=today,
    )


def extract(client: genai.Client, model: str, provider: dict, today: str) -> str:
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
    return text


def write_page(provider: dict, body: str, timestamp: str) -> Path:
    label = provider.get("label", "")
    label_suffix = f" ({label})" if label and label != provider["name"] else ""
    page = TEMPLATE.format(
        name=provider["name"],
        slug=provider["slug"],
        timestamp=timestamp,
        sources_yaml=render_sources_yaml(provider["urls"]),
        label_suffix=label_suffix,
        body=body.strip(),
    )
    out = PROVIDERS_DIR / f"{provider['slug']}.md"
    out.write_text(page)
    return out


def main() -> int:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY is not set", file=sys.stderr)
        return 2

    model = os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)
    sources = json.loads(SOURCES_PATH.read_text())

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
    for slug, provider in targets.items():
        print(f"→ {slug} ({provider['name']})")
        try:
            body = extract(client, model, provider, today)
            path = write_page(provider, body, timestamp)
            print(f"  wrote {path.relative_to(ROOT)}")
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}", file=sys.stderr)
            failures.append(slug)

    if failures:
        print(f"\n{len(failures)} provider(s) failed: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
