---
provider: DeepSeek
slug: deepseek
last_updated: 2026-05-18T15:35:15Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

# DeepSeek

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

### DeepSeek V4 Pro

- **Model ID**: `deepseek-v4-pro`
- **Context window**: 1M tokens
- **Max output**: 384K tokens
- **Input price**: $0.435 / 1M tokens
- **Output price**: $0.87 / 1M tokens
- **Cached input price**: $0.003625 / 1M tokens
- **Capabilities**: Json Output, Tool Calls, Chat Prefix Completion, FIM Completion
- **Notes**: Pricing reflects a 75% discount extended until 2026/05/31 15:59 UTC.

### DeepSeek V4 Flash

- **Model ID**: `deepseek-v4-flash`
- **Context window**: 1M tokens
- **Max output**: 384K tokens
- **Input price**: $0.14 / 1M tokens
- **Output price**: $0.28 / 1M tokens
- **Cached input price**: $0.0028 / 1M tokens
- **Capabilities**: Json Output, Tool Calls, Chat Prefix Completion, FIM Completion
- **Notes**: The model names `deepseek-chat` and `deepseek-reasoner` will be deprecated and correspond to this model's non-thinking and thinking modes.

## Notes

- Billing is based on the total number of input and output tokens.
- Fees are deducted from a topped-up balance or a granted balance, with granted balances used first.
- The input cache hit price for all models was reduced to 1/10 of the original launch price on 2026/4/26.
- The `deepseek-v4-pro` model is offered at a 75% discount until May 31, 2026.
- The API is available in both OpenAI and Anthropic formats.
- The `deepseek-chat` and `deepseek-reasoner` model aliases are being deprecated in favor of `deepseek-v4-flash`.
