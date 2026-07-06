---
provider: DeepSeek
slug: deepseek
last_updated: 2026-07-06T07:45:11Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-07-06T07:45:11Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
DeepSeek-V4 is the latest generation of models, featuring a unified architecture that supports both standard chat and extended thinking (reasoning) modes. The models are accessible via both OpenAI-compatible and Anthropic-compatible API formats.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | — | text, code | text | 1,000,000 | 384,000 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, prompt caching, thinking, FIM completion, chat prefix completion | Standard | 2500 concurrency | Input: $0.14<br>Cached: $0.0028<br>Output: $0.28 |
| `deepseek-v4-pro` | — | text, code | text | 1,000,000 | 384,000 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, prompt caching, thinking, FIM completion, chat prefix completion | Standard | 500 concurrency | Input: $0.435<br>Cached: $0.003625<br>Output: $0.87 |

#### Deprecated Models
These models are scheduled for retirement and currently serve as aliases for the `deepseek-v4-flash` model.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-chat` | `deepseek-v3` | text, code | text | 1,000,000 | 384,000 | Dec 2023 | Deprecated | Multilingual | function calling, structured outputs, streaming, system instructions, prompt caching | Standard | see Notes | Input: $0.14<br>Cached: $0.0028<br>Output: $0.28 |
| `deepseek-reasoner` | `deepseek-r1` | text, code | text | 1,000,000 | 384,000 | Oct 2023 | Deprecated | Multilingual | thinking, function calling, structured outputs, streaming, system instructions, prompt caching | Standard | see Notes | Input: $0.14<br>Cached: $0.0028<br>Output: $0.28 |

## Notes

- **Deprecation Schedule**: The model IDs `deepseek-chat` and `deepseek-reasoner` are scheduled for shutdown on **July 24, 2026, at 15:59 UTC**. Users are encouraged to migrate to `deepseek-v4-flash` or `deepseek-v4-pro`.
- **Thinking Mode**: Both V4 models support a "Thinking Mode" (reasoning) which can be toggled via the `thinking` parameter in the API request. When enabled, the model generates internal reasoning tokens before the final response. These tokens are billed at the standard output token rate.
- **Context Caching**: DeepSeek provides automatic context caching. If a prompt prefix matches a previously cached sequence (aligned to 64-token blocks), the "Cache Hit" price is applied. The cache is maintained automatically by the system with a typical TTL of 10 minutes.
- **API Compatibility**: The provider offers two base URLs:
    - OpenAI Format: `https://api.deepseek.com`
    - Anthropic Format: `https://api.deepseek.com/anthropic`
- **Rate Limits**: DeepSeek primarily uses concurrency-based rate limits rather than RPM/TPM. The default concurrency limit is 2500 for `deepseek-v4-flash` and 500 for `deepseek-v4-pro`.
- **FIM Completion**: Fill-In-the-Middle (FIM) is supported for code completion tasks in non-thinking mode only.
- **Free Tier**: New users typically receive a one-time credit of 2M to 5M tokens upon registration.
- **Billing**: Fees are deducted from a topped-up balance. Granted (free) balances are consumed before paid balances.
- **Data Residency**: DeepSeek is headquartered in China; data processing locations are not explicitly configurable via the public API.
