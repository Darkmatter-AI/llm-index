---
provider: xAI
slug: xai
last_updated: 2026-07-20T09:24:02Z
sources:
  - https://docs.x.ai/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-07-20T09:24:02Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
Flagship models designed for complex reasoning, coding, and agentic tasks. These models support multimodal inputs and advanced tool use.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | `grok-4.5-latest`, `grok-4.5-stable` | `text`, `image`, `PDF`, `code` | `text` | 500,000 | — | Feb 2026 | Stable | — |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | `function calling`, `structured outputs`, `streaming`, `system instructions`, `prompt caching`, `batch`, `code execution`, `web search`, `X search`, `vision`, `reasoning` (configurable), `context compaction`, `priority processing`, `agentic tool calling`, `file search` | `Standard`, `Priority` | see Notes | $2.00 / $6.00 |

### Voice & Audio
Dedicated APIs for real-time voice interaction, speech-to-text (STT), and text-to-speech (TTS).

| Model ID | Direction | Supported languages | Pricing |
| :--- | :--- | :--- | :--- |
| `grok-voice-agent` | Real-time conversation | — | $3.00 / hour |
| `grok-tts` | Text-to-Speech | — | $15.00 / 1M characters |
| `grok-stt` | Speech-to-Text (Batch) | — | $0.10 / hour |
| `grok-stt-streaming` | Speech-to-Text (Streaming) | — | $0.20 / hour |

### Image & Video
The Imagine API provides high-performance generation and editing capabilities for visual media.

| Model ID | Inputs | Output resolution(s) | Price |
| :--- | :--- | :--- | :--- |
| `grok-imagine` | `text`, `image` | 1K, 2K | $0.02 / image |
| `grok-video` | `text`, `image` | 480p, 720p, 1080p | $0.05 / second |

### Deprecated
Models that have been retired or are scheduled for shutdown.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `grok-2` | May 15, 2026 | `grok-4.5` |
| `grok-2-vision` | May 15, 2026 | `grok-4.5` |
| `grok-3` | May 15, 2026 | `grok-4.5` |
| `grok-beta` | May 15, 2026 | `grok-4.5` |
| `multi-agent-completions` | — | `grok-4.5` |

## Notes

- **Batch API**: Offers a 50% discount on standard pricing for requests processed within 24 hours.
- **Prompt Caching**: Supports automatic caching of frequently used context. Cache hits are billed at a 50% discount ($1.00 / 1M tokens for `grok-4.5`).
- **Rate Limits**: Tiers are based on monthly spend. Tier 1 (Trial): 100 RPM / 100,000 TPM. Tier 2: 500 RPM / 500,000 TPM. Tier 3: 1,000 RPM / 1,000,000 TPM. Tier 4: 2,000 RPM / 2,000,000 TPM. Tier 5: 5,000 RPM / 5,000,000 TPM.
- **Context Compaction**: A feature that automatically optimizes long-context windows to reduce token usage and improve performance.
- **Priority Processing**: A low-latency tier available for production workloads; pricing is typically 2x the standard rate for guaranteed throughput.
- **Vision Specs**: Maximum image size is 20MiB. Supports `jpg`, `jpeg`, and `png`. No limit on the number of images per request.
- **Search Tools**: Real-time data access requires enabling `web_search` or `x_search` tools; the model has no native knowledge of events post-cutoff.
- **Logprobs**: Note that `logprobs` and `top_logprobs` are not supported for models `grok-4.20` and newer.
