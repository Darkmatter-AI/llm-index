---
provider: DeepSeek
slug: deepseek
last_updated: 2026-05-18T17:31:04Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-05-18T17:31:04Z`

## Models

### Chat Models

| Model | Capabilities | Input ($/MTok, Cache Miss) | Input ($/MTok, Cache Hit) | Output ($/MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | reasoning, JSON output, tools | $0.14 | $0.0028 | $0.28 |
| `deepseek-v4-pro` | reasoning, JSON output, tools | $0.435 | $0.003625 | $0.87 |

## Notes

- Billing is based on the total number of input and output tokens.
- A significant discount is applied to input tokens that are a "cache hit".
- The `deepseek-v4-pro` model is offered at a 75% discount, which has been extended until 2026-05-31 15:59 UTC.
- The model names `deepseek-chat` and `deepseek-reasoner` are deprecated and correspond to the non-thinking and thinking modes of `deepseek-v4-flash`, respectively.
- Fees are deducted from a topped-up balance or a granted balance, with the granted balance being used first.
- Both models support a "Thinking Mode" for more complex tasks.
