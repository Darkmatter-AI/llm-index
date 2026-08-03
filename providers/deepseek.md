---
provider: DeepSeek
slug: deepseek
last_updated: 2026-08-03T09:55:07Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-08-03T09:55:07Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning

DeepSeek V4 introduces a unified architecture supporting both standard chat and high-compute "thinking" (reasoning) modes. These models feature a significantly expanded context window and high-capacity output limits compared to previous generations.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `DeepSeek-V4-Flash-0731` | text | text | 1,048,576 | 384,000 | — | Stable | — |
| `deepseek-v4-pro` | `DeepSeek-V4-Pro` | text | text | 1,048,576 | 384,000 | — | Stable | — |

| Model ID | Capabilities | Latency Tier / SLA | Rate Limits |
| :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | thinking, json output, tool calls, responses api, anthropic api, chat prefix completion, fim completion, prompt caching | Standard | Concurrency: 2500 |
| `deepseek-v4-pro` | thinking, json output, tool calls, anthropic api, chat prefix completion, fim completion, prompt caching | Standard | Concurrency: 500 |

| Model ID | Tier | Input $/MTok | Cached Input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | Standard (Off-peak) | $0.14 | $0.0028 | $0.28 |
| `deepseek-v4-flash` | Peak (2x) | $0.28 | $0.0056 | $0.56 |
| `deepseek-v4-pro` | Standard (Off-peak) | $0.435 | $0.003625 | $0.87 |
| `deepseek-v4-pro` | Peak (2x) | $0.87 | $0.00725 | $1.74 |

## Notes

- **Peak Pricing**: DeepSeek applies a 2x multiplier to all billing items during peak hours: 9:00–12:00 and 14:00–18:00 (Beijing Time, UTC+8) daily.
- **Prompt Caching**: Caching is automatic and integrated into the pricing model. "Cache Hit" rates apply to tokens already present in the provider's cache from previous requests.
- **Thinking Mode**: Both V4 models support a "thinking" mode (enabled by default) for complex reasoning tasks. Users can toggle this off for standard low-latency chat.
- **API Compatibility**: The DeepSeek API provides a native OpenAI-compatible format and a dedicated Anthropic-compatible API endpoint (`https://api.deepseek.com/anthropic`) for easier migration.
- **Responses API**: The `deepseek-v4-flash` model supports a specialized Responses API for optimized long-form generation; support for the `pro` model is scheduled for early August 2026.
- **Completion Betas**: Chat Prefix Completion and FIM (Fill-In-the-Middle) Completion are currently in Beta and are only supported in non-thinking mode.
- **Billing**: Fees are deducted from a topped-up balance. Granted (free) balances are consumed before paid balances.
- **Rate Limits**: Limits are primarily managed via concurrency (simultaneous requests) rather than traditional RPM/TPM tiers, with Flash allowing significantly higher throughput than Pro.
