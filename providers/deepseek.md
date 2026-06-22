---
provider: DeepSeek
slug: deepseek
last_updated: 2026-06-22T08:17:54Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-06-22T08:17:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
DeepSeek-V4 is the latest generation of models, featuring a unified architecture that supports both standard chat and extended thinking (reasoning) modes. The legacy model IDs `deepseek-chat` and `deepseek-reasoner` are maintained for compatibility but are scheduled for deprecation.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `deepseek-chat` (non-thinking), `deepseek-reasoner` (thinking) | `text`, `code` | `text` | 1,048,576 | 393,216 | — | Stable | — |
| `deepseek-v4-pro` | — | `text`, `code` | `text` | 1,048,576 | 393,216 | — | Stable | — |

#### Capabilities & Pricing

| Model ID | Capabilities | Latency tier | Rate limits | Input $/MTok | Cached $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `thinking`, `json output`, `tool calls`, `chat prefix completion`, `fim completion`, `context caching`, `streaming`, `system instructions` | Standard | 2500 Concurrency | 0.14 | 0.0028 | 0.28 |
| `deepseek-v4-pro` | `thinking`, `json output`, `tool calls`, `chat prefix completion`, `fim completion`, `context caching`, `streaming`, `system instructions` | Standard | 500 Concurrency | 0.435 | 0.003625 | 0.87 |

### Deprecated
The following model IDs are scheduled for retirement. Users are encouraged to migrate to the `deepseek-v4` series.

| Model ID | Replacement | Retirement Date |
| :--- | :--- | :--- |
| `deepseek-chat` | `deepseek-v4-flash` (non-thinking mode) | 2026-07-24 |
| `deepseek-reasoner` | `deepseek-v4-flash` (thinking mode) | 2026-07-24 |

## Notes

- **Thinking Mode**: DeepSeek-V4 models support a togglable "thinking" mode for complex reasoning. This is enabled via the `thinking: {"type": "enabled"}` parameter in the API request. Reasoning tokens are billed at the standard output rate.
- **Prompt Caching**: Context caching is automatic. When a prompt prefix matches a previously cached sequence, the "Cache Hit" pricing is applied. The minimum cacheable block size and TTL are managed internally by the provider.
- **Legacy Compatibility**: The `deepseek-chat` and `deepseek-reasoner` IDs currently point to the non-thinking and thinking modes of `deepseek-v4-flash` respectively to ensure zero-code migration until their retirement in July 2026.
- **Billing**: DeepSeek operates on a pre-paid balance system. Fees are deducted in real-time based on token usage. Granted (free) balances are consumed before topped-up balances.
- **Free Tier**: New users typically receive a starting balance (e.g., 5M tokens) upon registration, valid for a limited duration (usually 1 month).
- **Rate Limits**: Limits are primarily enforced via concurrency (simultaneous requests). `deepseek-v4-flash` allows up to 2500 concurrent requests, while `deepseek-v4-pro` is limited to 500.
- **API Compatibility**: The API is fully compatible with OpenAI and Anthropic request formats. Base URLs are `https://api.deepseek.com` (OpenAI) and `https://api.deepseek.com/anthropic` (Anthropic).
- **FIM Support**: Fill-In-the-Middle (FIM) completion is available in Beta for both V4 models but is restricted to non-thinking mode only.
