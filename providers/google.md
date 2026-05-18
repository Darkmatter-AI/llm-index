---
provider: Google
slug: google
last_updated: 2026-05-18T16:11:16Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-05-18T16:11:16Z`

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Gemini 2.5 Pro | `` `gemini-2.5-pro` (>200K) `` | >200K | — | $2.50 | $15.00 | $0.25 | vision, audio, reasoning | — |
| Gemini 2.5 Pro | `` `gemini-2.5-pro` (≤200K) `` | 200K | — | $1.25 | $10.00 | $0.125 | vision, audio, reasoning | — |
| Gemini 2.5 Flash | `` `gemini-2.5-flash` `` | 1M | — | $0.30 | $2.50 | $0.03 | vision, audio, reasoning | — |
| Gemini 3.1 Flash-Lite | `` `gemini-3.1-flash-lite` `` | — | — | $0.25 | $1.50 | $0.025 | vision, audio, tools | — |
| Gemini 2.5 Flash-Lite | `` `gemini-2.5-flash-lite` `` | — | — | $0.10 | $0.40 | $0.01 | vision, audio | — |

## Notes

*   A free tier with limited access is available for developers and small projects.
*   The Batch API offers a 50% cost reduction on standard pricing for eligible models.
*   Context caching is a paid feature that can lower costs for prompts with recurring prefixes.
*   Fine-tuning is not listed as a generally available feature for current models.
*   Stable model versions do not change, while `latest` tag aliases are updated with a two-week notice.
*   Model availability may differ across various regions.
*   Deprecated models are shut down after a notice period; for example, Gemini 2.0 Flash and Flash-Lite are scheduled for shutdown on June 1, 2026.
