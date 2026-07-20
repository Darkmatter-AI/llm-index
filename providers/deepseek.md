---
provider: DeepSeek
slug: deepseek
last_updated: 2026-07-20T09:24:02Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-07-20T09:24:02Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning

DeepSeek's V4 generation introduces a unified architecture where models support both standard chat and "Thinking Mode" (reasoning) via a single API endpoint. The models feature a massive 1M token context window and significantly increased output limits.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-pro` | — | `text` | `text` | 1,048,576 | 384,000 | — | `Stable` | Multilingual |
| `deepseek-v4-flash` | — | `text` | `text` | 1,048,576 | 384,000 | — | `Stable` | Multilingual |

| Model ID | Capabilities | Latency tier / SLA | Rate limits |
| :--- | :--- | :--- | :--- |
| `deepseek-v4-pro` | `thinking`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `chat prefix completion`, `FIM completion` (non-thinking only) | `Standard` | Concurrency: 500 |
| `deepseek-v4-flash` | `thinking`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `chat prefix completion`, `FIM completion` (non-thinking only) | `Fast` | Concurrency: 2,500 |

#### Pricing

| Model ID | Tier | Input $/MTok | Cached-input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-pro` | Standard | $0.435 | $0.003625 | $0.87 |
| `deepseek-v4-flash` | Standard | $0.14 | $0.0028 | $0.28 |

### Deprecated

These models are legacy identifiers that have been mapped to the V4 Flash architecture. They are scheduled for retirement.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-chat` | Maps to `deepseek-v4-flash` (non-thinking) | `text` | `text` | 65,536 | 8,192 | Oct 2024 | `Deprecated` (2026-07-24) | Multilingual |
| `deepseek-reasoner` | Maps to `deepseek-v4-flash` (thinking) | `text` | `text` | 65,536 | 8,192 | Oct 2024 | `Deprecated` (2026-07-24) | Multilingual |

| Model ID | Capabilities | Latency tier / SLA | Rate limits |
| :--- | :--- | :--- | :--- |
| `deepseek-chat` | `function calling`, `structured outputs`, `streaming`, `prompt caching` | `Fast` | see Notes |
| `deepseek-reasoner` | `thinking`, `streaming`, `prompt caching` | `Moderate` | see Notes |

#### Pricing

| Model ID | Tier | Input $/MTok | Cached-input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-chat` | Standard | $0.14 | $0.014 | $0.28 |
| `deepseek-reasoner` | Standard | $0.55 | $0.14 | $2.19 |

## Notes

- **Prompt Caching**: DeepSeek employs automatic context caching. When a prompt prefix matches a previously cached sequence, the "Cache Hit" price is applied. The discount is approximately 98-99% compared to a cache miss.
- **Thinking Mode**: For V4 models, "Thinking" (reasoning) is a toggleable mode rather than a separate model. Reasoning tokens generated during this mode are billed at the standard output token rate.
- **Anthropic Compatibility**: DeepSeek provides an Anthropic-compatible API endpoint at `https://api.deepseek.com/anthropic` for easier migration from Claude models.
- **Rate Limits**: Beyond the concurrency limits of 2,500 (Flash) and 500 (Pro), DeepSeek uses a tiered system based on account balance. Default limits for new accounts are typically 1,000 RPM and 100K TPM, increasing as the account is topped up.
- **FIM Completion**: Fill-In-the-Middle (FIM) is supported for code completion tasks but is restricted to non-thinking modes.
- **Chat Prefix Completion**: Supports pre-filling the assistant's response to guide the model's output style or format.
- **Open Source**: DeepSeek frequently releases model weights (e.g., DeepSeek-V3, DeepSeek-R1) for local hosting, though the API provides the most optimized versions (V4).
