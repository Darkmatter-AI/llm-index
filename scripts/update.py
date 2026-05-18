"""Daily updater for provider markdown pages.

Reads scripts/sources.json, asks Gemini to read each provider's official pricing/models
pages via the URL-context tool, and rewrites the corresponding providers/<slug>.md.

Required env:
  GEMINI_API_KEY   API key for Google AI Studio.
  GEMINI_MODEL     Optional. Defaults to gemini-2.5-pro.

Usage:
  python scripts/update.py                # update all providers
  python scripts/update.py anthropic gpt  # update specific slugs
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

For each generally-available model, an H3 with the model's display name. Under it, a bulleted list:
- **Model ID**: the exact API identifier (verbatim from docs)
- **Context window**: input token limit
- **Max output**: output token limit if listed
- **Input price**: USD per 1M input tokens
- **Output price**: USD per 1M output tokens
- **Cached input price**: USD per 1M cached input tokens, if offered
- **Capabilities**: vision, tool use, reasoning, audio, etc. — short comma list
- **Knowledge cutoff**: month/year if listed
- **Notes**: one short line for anything notable (deprecation date, preview status, regional limits)

Group models in a sensible order (newest/most capable first). Omit fields the provider does not publish — do **not** invent values. If a price is tiered (e.g. by context length), include all tiers as sub-bullets.

## Notes

A short bulleted list of provider-level facts that matter for picking a model: batch API discounts, prompt-caching mechanics, fine-tuning availability, free tiers, regional restrictions, deprecation policies. Three to seven bullets, each one line.

Rules:
- Use only data visible at the URLs above. Do not pull from training data.
- Keep numbers exact (`$1.25 / 1M tokens`, not "around a buck").
- No emojis. No marketing copy. No closing paragraph.
- If a page is unreachable or empty, write a single line under the relevant section: `_Source unreachable on {today}._`
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
