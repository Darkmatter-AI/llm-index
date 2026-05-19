---
provider: xAI
slug: xai
last_updated: 2026-05-19T11:54:43Z
sources:
  - https://docs.x.ai/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-05-19T11:54:43Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning
The Grok series provides high-intelligence text and vision processing with integrated tools for web search and code execution. Grok 4.3 is the current flagship model, supporting a massive 1-million-token context window and configurable reasoning capabilities.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.3` | `grok-4.3-latest`, `grok-4.3-20260515` | `text`, `image` | `text` | 1,048,576 | — | Nov 2024 | Stable |
| `grok-3` | `grok-3-latest` | `text`, `image` | `text` | 131,072 | — | Nov 2024 | Stable |

| Model ID | Languages | Capabilities | Latency Tier | Pricing (Input/MTok) | Pricing (Output/MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.3` | — | `function calling`, `structured outputs`, `streaming`, `system instructions`, `prompt caching`, `batch`, `code execution`, `web search`, `X search`, `reasoning`, `vision` | — | $1.25 | $2.50 |
| `grok-3` | — | `function calling`, `structured outputs`, `streaming`, `system instructions`, `prompt caching`, `batch`, `code execution`, `web search`, `X search`, `vision` | — | — | — |

### Voice
The Grok Voice API provides real-time conversational capabilities, including speech-to-text (STT) and text-to-speech (TTS).

| Model ID | Direction | Supported Languages | Latency | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `grok-voice-agent` | Multimodal (Speech-to-Speech) | — | Sub-second | $3.00 / hour |
| `grok-tts` | Text-to-Speech | — | Sub-second | $15.00 / 1M characters |
| `grok-stt` | Speech-to-Text | — | — | $0.10 / hour |

### Image & Video (Imagine API)
The Imagine API handles generation and editing for visual media.

| Model ID | Inputs | Output Resolution | Release Stage | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `grok-imagine-image` | `text`, `image` | 1K, 2K | Stable | $0.02 / image |
| `grok-imagine-video` | `text`, `image` | 480p, 720p | Stable | $0.05 / second |

### Deprecated
The following models were retired on **May 15, 2026**. Requests to these slugs are automatically redirected to `grok-4.3` and billed at `grok-4.3` rates.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `grok-4-1-fast` | May 15, 2026 | `grok-4.3` |
| `grok-4-fast` | May 15, 2026 | `grok-4.3` |
| `grok-4` | May 15, 2026 | `grok-4.3` |
| `grok-code-fast-1` | May 15, 2026 | `grok-4.3` |
| `grok-imagine-image-pro` | May 15, 2026 | `grok-imagine-image` |

## Notes

*   **Knowledge Cutoff**: Grok 3 and Grok 4 models have a training data cutoff of November 2024. Real-time information must be accessed via the `web search` or `X search` tools.
*   **Prompt Caching**: Supported for Grok 4.3 and Grok 3. Caching is typically triggered for prompts exceeding a specific token threshold (e.g., 1,024 tokens) and offers a discount on input pricing.
*   **Batch API**: A Batch API is available for non-latency-sensitive tasks, typically offering a 50% discount compared to standard inference rates.
*   **Vision Limits**: Maximum image size is 20MiB per file. There is no documented limit on the number of images per request. Supported formats include `jpg`, `jpeg`, and `png`.
*   **Logprobs**: `logprobs` and `top_logprobs` are explicitly not supported for models `grok-4.20` and newer; these parameters are silently ignored.
*   **Role Flexibility**: xAI chat models do not enforce strict role ordering; `system`, `user`, and `assistant` roles can be mixed in any sequence.
*   **Rate Limits**: xAI uses a tiered system (Tier 1 through Tier 5) based on usage history and prepayments. Specific RPM/TPM limits are viewable in the API Console under the "Rate Limits" tab.
*   **Reasoning Mode**: Grok 4.3 supports a configurable reasoning mode, allowing users to toggle between standard fast responses and extended thinking for complex tasks.
