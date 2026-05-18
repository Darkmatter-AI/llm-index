---
provider: Google
slug: google
last_updated: 2026-05-18T15:48:38Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-05-18T15:48:38Z`

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gemini 3.1 Pro | `` `gemini-3.1-pro-preview` (>200K) `` | >200K | — | $4.00 | $18.00 | $0.40 | vision, tools | — |
| Gemini 3.1 Pro | `` `gemini-3.1-pro-preview` (≤200K) `` | 200K | — | $2.00 | $12.00 | $0.20 | vision, tools | — |
| Gemini 2.5 Pro | `` `gemini-2.5-pro` (>200K) `` | >200K | — | $2.50 | $15.00 | $0.25 | vision, reasoning, coding | — |
| Gemini 2.5 Pro | `` `gemini-2.5-pro` (≤200K) `` | 200K | — | $1.25 | $10.00 | $0.125 | vision, reasoning, coding | — |
| Gemini 2.5 Flash | `` `gemini-2.5-flash` `` | 1M | — | $0.30 | $2.50 | $0.03 | vision, audio | — |
| Gemini 3.1 Flash-Lite | `` `gemini-3.1-flash-lite` `` | — | — | $0.25 | $1.50 | $0.025 | vision, audio | — |
| Gemini 2.5 Flash-Lite | `` `gemini-2.5-flash-lite` `` | — | — | $0.10 | $0.40 | $0.01 | vision, audio | — |

## Notes

*   A free tier is available with limited access to certain models.
*   The Batch API offers a 50% cost reduction on standard pricing.
*   Context caching is available on the paid tier to reduce costs for frequently used prefixes.
*   Preview models may change and will be deprecated with at least two weeks' notice.
*   Some models support grounding with Google Search and Google Maps, which may incur separate charges.
*   Model availability is subject to specified regions.
*   Deprecated models, such as Gemini 2.0 Flash, have published shutdown dates.
