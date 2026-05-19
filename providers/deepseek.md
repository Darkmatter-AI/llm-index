---
provider: DeepSeek
slug: deepseek
last_updated: 2026-05-19T11:27:53Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-05-19T11:27:53Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
DeepSeek's V4 series provides unified models capable of both standard chat and extended reasoning ("Thinking Mode"). The models are optimized for high-throughput and long-context tasks, featuring a native Fill-In-the-Middle (FIM) API for coding use cases.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `deepseek-chat` (non-thinking), `deepseek-reasoner` (thinking) | `text`, `code` | `text` | `1,048,576` | `393,216` | — | `Stable` |
| `deepseek-v4-pro` | — | `text`, `code` | `text` | `1,048,576` | `393,216` | — | `Stable` |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | — | `thinking`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `chat prefix completion`, `fim completion` | `Fastest` | see Notes |
| `deepseek-v4-pro` | — | `thinking`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `chat prefix completion`, `fim completion` | `Moderate` | see Notes |

**Pricing**

| Model ID | Tier | Input $/MTok | Cached Input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | Standard | `$0.14` | `$0.0028` | `$0.28` |
| `deepseek-v4-pro` | Discount (until 2026-05-31) | `$0.435` | `$0.0145` | `$0.87` |
| `deepseek-v4-pro` | Standard | `$1.74` | `$0.058` | `$3.48` |

## Notes

*   **Thinking Mode**: Both V4 models support a "Thinking Mode" that can be toggled via API parameters. When enabled, the model performs extended reasoning before responding. The `deepseek-reasoner` alias defaults to this mode on `deepseek-v4-flash`.
*   **Prompt Caching**: DeepSeek employs a disk-based prompt caching system. Cache hits are significantly cheaper than misses: 1/50th the price for the Flash model and 1/30th the price for the Pro model. Cache TTL and management are handled automatically by the provider.
*   **Deprecation Policy**: The legacy model IDs `deepseek-chat` and `deepseek-reasoner` are deprecated and now serve as aliases for the non-thinking and thinking modes of `deepseek-v4-flash`, respectively.
*   **Anthropic Compatibility**: DeepSeek provides an Anthropic-compatible API endpoint at `https://api.deepseek.com/anthropic` to facilitate easier migration for users of Claude models.
*   **Coding Features**: The models support specialized coding features including `fim completion` (Fill-In-the-Middle) for code ghostwriting and `chat prefix completion` for steering model responses.
*   **Rate Limits**: Limits are determined by the user's account tier (based on total top-up amount). Standard Pay-as-you-go limits typically range from 1,000 to 10,000 RPM and 100K to 1M TPM depending on the specific model and account standing.
*   **Billing**: Fees are deducted from a pre-paid balance. Granted (free) balances are consumed before topped-up balances.
*   **Regional Availability**: Primary API services are hosted globally with a base URL of `https://api.deepseek.com`. Localized endpoints for the Chinese market are available via `https://api.deepseek.com/v1`.
