---
provider: DeepSeek
slug: deepseek
last_updated: 2026-05-18T17:18:48Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-05-18T17:18:48Z`  ·  [JSON](../data/deepseek.json)

## Models

### Chat / completion

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DeepSeek V4 Pro | `deepseek-v4-pro` | 1M | 384K | $1.74 | $3.48 | $0.0145 | tools, json | — |
| DeepSeek V4 Flash | `deepseek-v4-flash` | 1M | 384K | $0.14 | $0.28 | $0.0028 | tools, json | — |

## Notes

- Billing is based on the total number of input and output tokens.
- Fees are deducted from a user's topped-up or granted balance, with granted balances being used first.
- DeepSeek supports context caching, offering a significantly reduced price for cached input tokens (cache hits).
- The input cache hit price for all models was reduced to 1/10 of the original launch price as of 2026/04/26.
- The model names `deepseek-chat` and `deepseek-reasoner` are deprecated and are now aliases for the `deepseek-v4-flash` model.

