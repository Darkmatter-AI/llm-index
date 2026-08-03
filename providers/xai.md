---
provider: xAI
slug: xai
last_updated: 2026-08-03T09:55:07Z
sources:
  - https://docs.x.ai/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-08-03T09:55:07Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
xAI's flagship models are designed for agentic workflows, complex reasoning, and multimodal understanding. The current generation is the Grok 4 series, which consolidated previous specialized "vision" and "beta" models into a single unified flagship.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | `grok-4.5-latest`, `grok-4.5-<date>` | text, image | text | 500,000 | — | Feb 2026 | Stable | — |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input) | Pricing (Output) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, reasoning, vision, multi-agent, context compaction, priority processing | Fastest | see Notes | $2.00 / MTok | $6.00 / MTok |

### Image & Video
The Grok Imagine API provides high-speed generation and editing capabilities for visual media.

| Model ID | Inputs | Output resolution(s) | Price |
| :--- | :--- | :--- | :--- |
| `grok-imagine` | text, image | 1K, 2K | $0.02 / image |
| `grok-imagine` | text, image | 480p, 720p, 1080p | $0.05 / second (Video) |

### Voice & Speech
The Grok Voice API supports real-time conversational agents and asynchronous speech processing.

| Model ID | Direction | Supported languages | Price |
| :--- | :--- | :--- | :--- |
| `grok-voice` | Speech-to-Speech (Agent) | — | $0.05 / minute |
| `grok-voice` | Text-to-Speech (TTS) | — | $15.00 / 1M characters |
| `grok-voice` | Speech-to-Text (STT) | — | $0.10 / hour (Batch) |
| `grok-voice` | Speech-to-Text (STT) | — | $0.20 / hour (Streaming) |

### Deprecated
Older models were retired on May 15, 2026. Users are encouraged to migrate to the Responses API and the Grok 4.5 flagship.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `grok-2` | May 15, 2026 | `grok-4.5` |
| `grok-2-1212` | May 15, 2026 | `grok-4.5` |
| `grok-beta` | May 15, 2026 | `grok-4.5` |
| `grok-vision-beta` | May 15, 2026 | `grok-4.5` |

## Notes

- **Rate Limits**: xAI uses a tiered system for rate limits (Tier 1 through Tier 5). Limits are typically defined by Requests Per Minute (RPM) and Tokens Per Minute (TPM). Specific caps are visible in the API Console under the "Limits" tab.
- **Prompt Caching**: Supported on `grok-4.5`. Caching is automatic for repeated prefixes; however, specific TTL and discount percentages are not publicly detailed in the primary model index.
- **Batch API**: Supports "Deferred Completions" for non-latency-sensitive tasks.
- **Vision Specs**: Supports `jpg`, `jpeg`, and `png`. Maximum file size is 20MiB per image. There is no documented limit on the number of images per request.
- **Search Grounding**: Real-time data access requires enabling `web_search` or `x_search` tools; the model does not have native real-time access without these tools.
- **Logprobs**: Note that `logprobs` and `top_logprobs` are explicitly not supported for models `grok-4.20` and newer; these parameters are silently ignored.
- **Role Flexibility**: The Responses API allows for any sequence of `system`, `user`, or `assistant` roles without strict ordering requirements.
- **Context Compaction**: A specialized feature for long-context management that allows the model to summarize or compress previous turns to maintain performance within the 500k window.
- **Priority Processing**: Available for enterprise users to ensure lower latency during peak demand periods.
