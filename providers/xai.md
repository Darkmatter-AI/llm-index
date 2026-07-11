---
provider: xAI
slug: xai
last_updated: 2026-07-11T07:17:09Z
sources:
  - https://docs.x.ai/docs/models
  - https://docs.x.ai/developers/grok-4-5
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-07-11T07:17:09Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning

Models designed for general-purpose conversation, complex reasoning, and multi-modal understanding. Grok 4.5 is the flagship model, while Grok 4.3 is the previous flagship and Grok 4.20 introduces advanced reasoning capabilities with specific constraints on logprobs.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Rate Limits | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | `grok-4.5-latest` | text, image | text | 500,000 (requests above 200,000 tokens billed at higher-context rates) | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, reasoning (configurable, supports non-reasoning and reasoning modes), vision, agentic tool calling | Standard, Priority, Batch | see Notes | Input: $2.00<br>Output: $6.00<br>Cached input: $0.50 |
| `grok-4.3` | `grok-4.3-latest`, `grok-4.3-20260529` | text, image | text | 1,048,576 | — | Nov 2024 | Stable | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, reasoning (configurable), vision, multi-agent | Standard, Priority, Batch | see Notes | Input: $1.25<br>Output: $2.50 |
| `grok-4.20` | `grok-4.20-latest` | text, image | text | 1,048,576 | — | Nov 2024 | Preview | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, reasoning, vision, multi-agent, Not: logprobs | Standard, Priority, Batch | see Notes | Input: $1.25<br>Output: $2.50 |
| `grok-3` | `grok-3-latest` | text, image | text | — | — | Nov 2024 | Stable | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, vision | Standard, Priority, Batch | see Notes | — |

### Specialized

Models optimized for specific workflows, such as agentic coding or high-efficiency tasks.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Rate Limits | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-build-0.1` | `grok-build-latest` | text, code | text, code | 262,144 | — | Nov 2024 | Stable | — | agentic coding, function calling, code execution, streaming, system instructions, prompt caching, batch, context compaction | Standard, Priority, Batch | see Notes | Input: $1.00<br>Output: $2.00 |

### Image & Video

The Imagine API provides industry-leading speeds for generating and editing visual content.

| Model ID | Inputs | Output Resolution(s) | Price |
| :--- | :--- | :--- | :--- |
| `grok-imagine` | text, image | 1K, 2K | $0.02 / image |
| `grok-video` | text, image | 480p, 720p, 1080p | $0.05 / second |

### Voice

The Voice API supports real-time conversational agents and high-fidelity speech processing.

| Model ID | Direction | Supported Languages | Price |
| :--- | :--- | :--- | :--- |
| `grok-voice-agent` | bidirectional | — | $3.00 / hour |
| `grok-tts` | text-to-speech | — | $15.00 / 1M characters |
| `grok-stt-batch` | speech-to-text | — | $0.10 / hour |
| `grok-stt-streaming` | speech-to-text | — | $0.20 / hour |

### Deprecated

Models that have been superseded by newer generations and are scheduled for retirement.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `grok-2-1212` | May 15, 2026 | `grok-4.3` |
| `grok-2-mini-1212` | May 15, 2026 | `grok-build-0.1` |
| `grok-beta` | May 15, 2026 | `grok-4.3` |
| `grok-vision-beta` | May 15, 2026 | `grok-4.3` |

## Notes

- **grok-4.5 Higher-Context Billing**: Requests above 200,000 tokens are billed at higher-context rates.
- **Knowledge Cutoff**: All Grok 3 and Grok 4 generation models have a reliable knowledge cutoff of November 2024. Real-time data access requires enabling `Web Search` or `X Search` tools.
- **Prompt Caching**: Supported on all Grok 4 and Grok Build models. Caching reduces latency and cost for repeated context; specific TTL and discount rates are applied automatically based on usage patterns.
- **Batch API**: Offers a 50% discount on standard inference rates for non-urgent workloads processed within 24 hours.
- **Rate Limit Tiers**: xAI uses a tiered system (Tier 1 through Tier 5) based on monthly spend. Limits are applied per-model and per-tier. For example, Tier 1 typically starts at 1,000 RPM while Tier 5 supports enterprise-scale throughput.
- **Image Input Specs**: Maximum image size is 20MiB. Supported formats include `jpg`, `jpeg`, and `png`. There is no limit on the number of images per request.
- **Logprobs**: Starting with `grok-4.20`, `logprobs` and `top_logprobs` are no longer supported and will be silently ignored if included in the request.
- **Reasoning Configuration**: Grok 4.3 supports configurable reasoning, allowing developers to adjust the depth of internal "thinking" steps for complex problem-solving.
- **Model Aliases**: The dateless ID (e.g., `grok-4.3`) points to the latest stable version. The `-latest` suffix points to the absolute newest release, including experimental updates. Dated snapshots (e.g., `grok-4.3-20260529`) are pinned for consistency.
