---
provider: DeepSeek
slug: deepseek
last_updated: 2026-07-27T10:00:03Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-07-27T10:00:03Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning

DeepSeek's fourth-generation models feature a unified architecture that supports both standard chat and high-effort reasoning ("thinking") within the same model ID. These models are accessible via both OpenAI-compatible and Anthropic-compatible API formats.

| Model ID | Aliases | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `deepseek-v4-flash-latest` | `text` | `text` | 1,048,576 | 384,000 | — | Stable | — |
| `deepseek-v4-pro` | `deepseek-v4-pro-latest` | `text` | `text` | 1,048,576 | 384,000 | — | Stable | — |

<br>

| Model ID | Capabilities | Latency Tier | Rate Limits (Concurrency) |
| :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `thinking`, `function calling`, `structured outputs`, `streaming`, `system instructions`, `caching`, `chat prefix completion`, `FIM completion` | Standard | 2,500 |
| `deepseek-v4-pro` | `thinking`, `function calling`, `structured outputs`, `streaming`, `system instructions`, `caching`, `chat prefix completion`, `FIM completion` | Standard | 500 |

#### Pricing

Prices are in USD per 1 million tokens.

| Model ID | Tier | Input (Cache Miss) | Input (Cache Hit) | Output |
| :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | Standard | $0.14 | $0.0028 | $0.28 |
| `deepseek-v4-pro` | Standard | $0.435 | $0.003625 | $0.87 |

### Specialized

#### Completion (Beta)

DeepSeek provides specialized endpoints for code-centric tasks like Fill-In-the-Middle (FIM).

| Model ID | Description | Capabilities | Pricing (Input/Output) |
| :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | FIM Completion | `FIM completion` (Non-thinking mode only) | Same as Chat |
| `deepseek-v4-pro` | FIM Completion | `FIM completion` (Non-thinking mode only) | Same as Chat |

## Notes

- **Thinking Mode**: DeepSeek V4 models support a "thinking" mode for complex reasoning. This is enabled by default but can be toggled via the `thinking` parameter (e.g., `{"type": "enabled"}`). Users can control reasoning depth using the `reasoning_effort` parameter (`low`, `medium`, `high`).
- **Prompt Caching**: The system automatically caches frequently used prefixes in 64-token blocks. Cache hits are billed at a significantly reduced rate (approx. 2% of the standard input price for Flash, 0.8% for Pro). There is no manual management required; caching is based on prefix matching.
- **API Compatibility**: The provider maintains two base URLs:
    - OpenAI Format: `https://api.deepseek.com`
    - Anthropic Format: `https://api.deepseek.com/anthropic`
- **Concurrency Limits**: Unlike traditional RPM/TPM limits, DeepSeek prioritizes concurrency-based limits. `deepseek-v4-flash` allows up to 2,500 concurrent requests, while `deepseek-v4-pro` allows 500.
- **Billing**: Fees are deducted from a topped-up balance. Granted (free) balances are consumed before paid balances.
- **FIM Completion**: Fill-In-the-Middle (FIM) is supported for code completion tasks but is restricted to non-thinking mode only.
- **Chat Prefix Completion**: Supports pre-filling the assistant's response to guide the model's output style or format.
