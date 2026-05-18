---
provider: Anthropic
slug: anthropic
last_updated: 2026-05-18T17:18:48Z
sources:
  - https://www.anthropic.com/pricing
  - https://docs.anthropic.com/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [docs.anthropic.com/en/docs/about-claude/models/overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-05-18T17:18:48Z`  ·  [JSON](../data/anthropic.json)

## Models

### Chat / completion

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 1M | 64K | $3 | $15 | $0.3 | vision, tools | Aug 2025 |
| Claude Sonnet 4.5 | `claude-sonnet-4-5` | — | — | $3 | $15 | $0.3 | vision, tools | — |
| Claude Sonnet 4 | `claude-sonnet-4` | — | — | $3 | $15 | $0.3 | vision, tools | — |

### Reasoning

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Opus 4.7 | `claude-opus-4-7` | 1M | 128K | $5 | $25 | $0.5 | vision, tools, reasoning | Jan 2026 |
| Claude Opus 4.6 | `claude-opus-4-6` | — | — | $5 | $25 | $0.5 | vision, tools, reasoning | — |
| Claude Opus 4.5 | `claude-opus-4-5` | — | — | $5 | $25 | $0.5 | vision, tools, reasoning | — |
| Claude Opus 4.1 | `claude-opus-4-1` | — | — | $15 | $75 | $1.5 | vision, tools, reasoning | — |
| Claude Opus 4 | `claude-opus-4` | — | — | $15 | $75 | $1.5 | vision, tools, reasoning | — |

### Realtime / audio

| Model | ID | Audio In $/MTok | Audio Out $/MTok | Text In $/MTok | Text Out $/MTok | Cached In $/MTok | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | — | — | $1 | $5 | — | Fastest, most cost-efficient model. |

## Notes

- Batch processing offers a 50% discount on API usage for asynchronous workloads.
- US-only inference is available at 1.1x pricing for input and output tokens.
- Prompt caching has a default 5-minute Time-To-Live (TTL), with extended options available.
- Anthropic maintains a model deprecation schedule, with details available on their documentation site.
- Additional platform features are priced separately: Managed Agents ($0.08/session-hour), Web search ($10/1k searches), and Code execution ($0.05/hour after a daily free tier).
- Fine-tuning is not offered as a generally available, priced feature on the provided pages.

