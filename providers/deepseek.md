---
provider: DeepSeek
slug: deepseek
last_updated: 2026-08-10T07:49:39Z
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · **DeepSeek** · [Mistral](mistral.md)

# DeepSeek

**Sources:** [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)  ·  **Updated:** `2026-08-10T07:49:39Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
DeepSeek V4 is the current generation of models, featuring native "Thinking Mode" (reasoning) and a massive 1M token context window. These models are accessible via both OpenAI-compatible and Anthropic-compatible API formats.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | `DeepSeek-V4-Flash-0731` | text, code | text | 1,048,576 | 384,000 | — | Stable | English, Chinese |
| `deepseek-v4-pro` | `DeepSeek-V4-Pro` | text, code | text | 1,048,576 | 384,000 | — | Stable | English, Chinese |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input Miss) | Pricing (Input Hit) | Pricing (Output) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-v4-flash` | JSON Output, Tool Calls, Responses API, Anthropic API, Chat Prefix Completion, FIM Completion, Thinking Mode, streaming, system instructions, prompt caching | Standard | 2500 Concurrency | $0.14 / MTok | $0.0028 / MTok | $0.28 / MTok |
| `deepseek-v4-pro` | JSON Output, Tool Calls, Anthropic API, Chat Prefix Completion, FIM Completion, Thinking Mode, streaming, system instructions, prompt caching | Standard | 500 Concurrency | $0.435 / MTok | $0.003625 / MTok | $0.87 / MTok |

## Notes

- **Thinking Mode**: Both V4 models support a native "Thinking Mode" (reasoning) which is enabled by default. It can be toggled via the `thinking: {"type": "enabled"}` parameter and adjusted using `reasoning_effort` (e.g., `high`).
- **Anthropic API Compatibility**: DeepSeek provides a dedicated base URL (`https://api.deepseek.com/anthropic`) that accepts Anthropic-formatted requests, allowing users to swap DeepSeek into Claude-based workflows (e.g., Claude Code, MCP) without code changes.
- **Context Caching**: Prompt caching is automatic and billed at a significantly reduced rate for "Cache Hits." The system uses a 64KB block-level matching mechanism.
- **Rate Limits**: DeepSeek has transitioned to a **Concurrency-based** rate limiting model rather than traditional RPM/TPM. `deepseek-v4-flash` allows up to 2500 simultaneous requests, while `deepseek-v4-pro` allows 500.
- **Responses API**: A specialized API for high-throughput or structured response handling, currently exclusive to the `deepseek-v4-flash` model (support for `pro` expected August 2026).
- **FIM Completion**: Fill-In-the-Middle (FIM) is supported for code completion tasks but is restricted to "Non-thinking mode" only.
- **Pricing Warning**: As of August 2026, DeepSeek has announced plans for a significant increase in API pricing in the near future; current rates are subject to change with official notice.
- **Max Output**: The models support an industry-leading output limit of 384,000 tokens per request, suitable for long-form generation and complex reasoning chains.
- **Billing**: Fees are deducted from a topped-up balance. Granted balances (free credits) are consumed before paid balances.
