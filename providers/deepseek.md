---
provider: DeepSeek
slug: deepseek
last_updated: 2026-05-18T15:48:38Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

# DeepSeek

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DeepSeek V4 Pro | `` `deepseek-v4-pro` `` | 1M | 384K | $0.435 | $0.87 | $0.003625 | JSON, tools, prefix completion, FIM | — |
| DeepSeek V4 Flash | `` `deepseek-v4-flash` `` | 1M | 384K | $0.14 | $0.28 | $0.0028 | JSON, tools, prefix completion, FIM | — |

## Notes

*   The `deepseek-v4-pro` model is offered at a 75% discount, which is extended until 2026/05/31 15:59 UTC.
*   All models feature context caching, with a significantly reduced price for cached input tokens (cache hits).
*   The model names `deepseek-chat` and `deepseek-reasoner` are being deprecated and will be replaced by `deepseek-v4-flash`.
*   Fees are deducted from a user's topped-up or granted balance, with granted balances being used first.
