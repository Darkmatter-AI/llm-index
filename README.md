# llm-index

Up-to-date catalog of LLM providers, models, pricing, and capabilities — refreshed weekly by a Gemini-powered pipeline.

**Live site:** https://darkmatter-ai.github.io/llm-index/

## Why

LLM training cutoffs mean assistants give stale model/pricing info. This repo solves that with a tiny dynamic source of truth:

1. A weekly GitHub Actions job uses Gemini's URL-context tool to read each provider's official pricing/models page.
2. Gemini extracts structured data and rewrites the markdown in `providers/`.
3. GitHub Pages serves the markdown as a public site any agent or human can read.
4. A bundled Claude Code skill in `skill/` tells agents to consult this site instead of relying on training data.

## Providers

- [Anthropic](providers/anthropic.md) — Claude
- [OpenAI](providers/openai.md) — GPT
- [Google](providers/google.md) — Gemini
- [xAI](providers/xai.md) — Grok
- [DeepSeek](providers/deepseek.md)
- [Mistral](providers/mistral.md)

## Repo layout

```
providers/         # generated markdown, one file per provider — table + notes
scripts/           # pipeline that updates providers/
  sources.json     # URLs Gemini reads per provider
  update.py        # Gemini extraction script (PEP 723 inline deps, run with uv)
skill/             # installable Claude Code skill that points agents here
.github/workflows/ # weekly cron
```

## Pipeline

Runs every Monday at 06:00 UTC via `.github/workflows/update.yml`. Reads `scripts/sources.json`, asks Gemini to extract model/pricing data from each provider's official pages using the URL-context tool, and commits any diffs to `providers/`.

The updater declares its dependencies inline (PEP 723) and is run with [uv](https://docs.astral.sh/uv/) — no `requirements.txt`, no virtualenv setup. Local invocation:

```bash
export GEMINI_API_KEY=...
uv run scripts/update.py                # all providers
uv run scripts/update.py anthropic openai
```

Required repo secret: `GEMINI_API_KEY`. To trigger manually: Actions → "Update provider data" → Run workflow.

## Skill

See [skill/README.md](skill/README.md) to install the Claude Code skill that biases agents toward this site.
