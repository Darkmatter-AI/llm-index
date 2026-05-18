---
provider: xAI
slug: xai
last_updated: 2026-05-18T16:11:16Z
sources:
  - https://docs.x.ai/docs/models
  - https://x.ai/api
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models), [x.ai/api](https://x.ai/api)  ·  **Updated:** `2026-05-18T16:11:16Z`

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Grok 4.3 | `` `grok-4.3` `` | 1M | — | $1.25 | $2.50 | — | vision, tool calling, reasoning | Nov 2024 |

## Notes

*   A Prompt Caching feature is available to reduce costs on repeated prefixes.
*   A Batch API is available for submitting a large number of requests asynchronously.
*   Requests to retired model IDs are automatically redirected to `grok-4.3` and billed at its standard rate.
*   Models require enabling a search tool (e.g., Web Search or X Search) to access real-time information.
*   Image inputs are supported for files up to 20MiB in JPG or PNG format.
*   The API is compatible with OpenAI and Anthropic SDKs.
