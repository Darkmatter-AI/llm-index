---
provider: xAI
slug: xai
last_updated: 2026-06-22T08:17:54Z
sources:
  - https://docs.x.ai/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-06-22T08:17:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
Models designed for general-purpose conversation, complex reasoning, and agentic workflows. Grok 4.3 is the flagship model, featuring a configurable reasoning engine and high-speed inference.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.3` | `grok-4.3-latest`, `grok-4.3-20260529` | `text`, `image` | `text` | 1,000,000 | — | Nov 2024 | Stable |
| `grok-4` | `grok-4-latest` | `text`, `image` | `text` | — | — | Nov 2024 | Stable |
| `grok-3` | `grok-3-latest` | `text`, `image` | `text` | — | — | Nov 2024 | Stable |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.3` | — | `agentic tool calling`, `reasoning`, `non-reasoning mode`, `function calling`, `web search`, `X search`, `code execution`, `collections search (RAG)`, `remote MCP tools`, `prompt caching`, `context compaction`, `priority processing`, `structured outputs`, `streaming`, `multi agent`, `vision` | Priority, Standard | see Notes | Input: $1.25<br>Output: $2.50 |
| `grok-4` | — | `function calling`, `web search`, `X search`, `code execution`, `prompt caching`, `structured outputs`, `streaming`, `vision` | Standard | see Notes | — |
| `grok-3` | — | `function calling`, `web search`, `X search`, `code execution`, `prompt caching`, `structured outputs`, `streaming`, `vision` | Standard | see Notes | — |

### Specialized
Models optimized for specific engineering and development tasks, such as agentic coding and repository-level understanding.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-build-0.1` | `grok-build-latest` | `text`, `code` | `text` | 256,000 | — | Nov 2024 | Preview |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-build-0.1` | — | `fast coding`, `agentic coding workflows`, `function calling`, `code execution`, `remote MCP tools`, `prompt caching`, `context compaction`, `priority processing`, `structured outputs`, `streaming` | Priority, Standard | see Notes | Input: $1.00<br>Output: $2.00 |

### Image & Video
The Imagine API provides high-speed generation and editing capabilities for visual media.

| Model ID | Inputs | Output resolution(s) | Price |
| :--- | :--- | :--- | :--- |
| `grok-imagine` | `text`, `image`, `image+mask` | 1K, 2K (Image), 480p, 720p (Video) | Image: $0.02 / image<br>Video: $0.05 / sec |

### Voice
The Voice API supports real-time conversational agents, high-fidelity text-to-speech, and asynchronous speech-to-text.

| Model ID | Direction | Supported languages | Price |
| :--- | :--- | :--- | :--- |
| `grok-voice` | `STT`, `TTS`, `Real-time Agent` | — | Agent: $3.00 / hour<br>TTS: $15.00 / 1M chars<br>STT (Batch): $0.10 / hour<br>STT (Streaming): $0.20 / hour |

### Deprecated
Models retired or scheduled for retirement.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `grok-2` | May 15, 2026 | `grok-4.3` |
| `grok-2-1212` | May 15, 2026 | `grok-4.3` |
| `grok-2-vision` | May 15, 2026 | `grok-4.3` |
| `grok-beta` | May 15, 2026 | `grok-4.3` |
| `grok-vision-beta` | May 15, 2026 | `grok-4.3` |

## Notes

- **Prompt Caching**: xAI supports automatic prompt caching for repeated prefixes. Cached input tokens are typically billed at a 50% discount compared to standard input rates.
- **Batch API**: Asynchronous batch processing is available for non-latency-sensitive workloads, offering a 50% discount on standard token pricing.
- **Rate Limits**: Limits are determined by account tiers (Tier 1 through Tier 5). Tier 1 typically starts at 100 RPM, while Tier 5 can reach 5,000+ RPM. Specific limits are visible in the API Console.
- **Logprobs**: `logprobs` and `top_logprobs` are not supported for models `grok-4.20` and newer; these parameters are silently ignored.
- **Image Constraints**: Maximum image size is 20MiB. There is no limit on the number of images per request. Supported formats include `jpg`, `jpeg`, and `png`.
- **Search Tools**: Grok models do not have access to real-time events unless `Web Search` or `X Search` tools are explicitly enabled in the request.
- **Reasoning Mode**: Grok 4.3 features a configurable reasoning engine. Users can toggle between a "non-reasoning" mode for speed and various reasoning levels for complex problem-solving.
- **Context Compaction**: A specialized feature for long-context management that optimizes token usage by compacting historical conversation data.
