---
provider: DeepSeek
slug: deepseek
last_updated: 2026-05-18T16:11:16Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-05-18T16:11:16Z`

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DeepSeek-V4-Pro | `deepseek-v4-pro` | 1M | 384K | $0.435 | $0.87 | $0.0145 | json, tools, chat prefix, FIM | — |
| DeepSeek-V4-Flash | `deepseek-v4-flash` | 1M | 384K | $0.14 | $0.28 | $0.0028 | json, tools, chat prefix, FIM | — |

## Notes

*   The `deepseek-v4-pro` model is offered at a 75% discount until May 31, 2026.
*   Input cache hit pricing is 1/10th of the launch price for all models.
*   Fees are deducted from your topped-up or granted balance, with granted balance used first.
*   The model IDs `deepseek-chat` and `deepseek-reasoner` are deprecated and correspond to `deepseek-v4-flash`.
*   Models support a "Thinking Mode" for complex tasks.
*   The API is available in both OpenAI and Anthropic formats.
