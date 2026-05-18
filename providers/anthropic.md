---
provider: Anthropic
slug: anthropic
last_updated: 2026-05-18T17:31:04Z
sources:
  - https://www.anthropic.com/pricing
  - https://docs.anthropic.com/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [docs.anthropic.com/en/docs/about-claude/models/overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-05-18T17:31:04Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Latest Models

| Model | Model ID | Capabilities | Input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| Claude Opus 4.7 | `claude-opus-4-7` | vision, agentic coding, complex reasoning | $5.00 | $25.00 |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | vision | $3.00 | $15.00 |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | vision | $1.00 | $5.00 |

### Legacy Models

| Model | Input $/MTok | Output $/MTok |
| :--- | :--- | :--- |
| Opus 4.6 | $5.00 | $25.00 |
| Sonnet 4.5 | $3.00 | $15.00 |
| Opus 4.5 | $5.00 | $25.00 |
| Opus 4.1 | $15.00 | $75.00 |
| Sonnet 4 | $3.00 | $15.00 |
| Opus 4 | $15.00 | $75.00 |

### Prompt Caching

| Model | Write $/MTok | Read $/MTok |
| :--- | :--- | :--- |
| Opus 4.7 | $6.25 | $0.50 |
| Sonnet 4.6 | $3.75 | $0.30 |
| Haiku 4.5 | $1.25 | $0.10 |
| Opus 4.6 | $6.25 | $0.50 |
| Sonnet 4.5 | $3.75 | $0.30 |
| Opus 4.5 | $6.25 | $0.50 |
| Opus 4.1 | $18.75 | $1.50 |
| Sonnet 4 | $3.75 | $0.30 |
| Opus 4 | $18.75 | $1.50 |

### Additional Services

| Service | Rate |
| :--- | :--- |
| Managed Agents | $0.08 per session-hour (active runtime) |
| Web search | $10.00 / 1K searches |
| Code execution | $0.05 per hour per container (after 50 free hours daily per org) |

## Notes

*   Asynchronous workloads using the Batch API receive a 50% discount on token prices.
*   US-only data residency is available for input and output tokens at a 1.1x price multiplier.
*   Prompt caching is available to reduce costs for repeated prefixes; rates are based on a 5-minute TTL.
*   Anthropic maintains a model deprecation policy and provides guidance for upgrading between model versions.
*   Service tiers (Priority, Standard, Batch) are available to balance performance, availability, and cost.
*   Model IDs are pinned snapshots; dateless formats (e.g., `claude-opus-4-7`) are also fixed snapshots, not evergreen pointers.
