---
provider: xAI
slug: xai
last_updated: 2026-07-27T10:00:03Z
sources:
  - https://docs.x.ai/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-07-27T10:00:03Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning

Grok 4.5 is the flagship model, designed for high-intelligence tasks including coding, agentic tool use, and complex reasoning. It features a significantly expanded context window and integrated vision capabilities.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | `grok-4.5-latest`, `grok-4.5-20260201` | `text`, `image` | `text` | 500,000 | — | Feb 2026 | Stable | — | function calling, structured outputs, streaming, prompt caching, batch, web search, X search, vision, reasoning, multi-agent, priority processing | Fastest | Input: $2.00<br>Output: $6.00 |

#### Reasoning Capabilities
Grok 4.5 supports **Configurable Reasoning**, allowing users to adjust the depth of thought for complex problem-solving. This is managed via the API to balance latency and intelligence.

### Image & Video

The Grok Imagine API provides industry-leading speeds for generating and editing visual content.

| Model ID | Inputs | Output resolution(s) | Price |
| :--- | :--- | :--- | :--- |
| `grok-imagine` | `text`, `image` | 1K, 2K | $0.02 / image |
| `grok-video` | `text`, `image` | 480p, 720p, 1080p | $0.05 / second |

**Supported Features:**
- **Image Generation & Editing**: Create new images or modify existing ones.
- **Multi-Image Editing**: Edit multiple images in a single session.
- **Video Generation**: Image-to-video, video editing, reference-to-video, and video extension.

### Speech & Audio

The Grok Voice API supports real-time conversational AI, high-fidelity text-to-speech, and robust speech-to-text.

| Model ID | Direction | Supported languages | Price |
| :--- | :--- | :--- | :--- |
| `grok-voice-agent` | Speech-to-Speech | — | $3.00 / hour |
| `grok-tts` | Text-to-Speech | — | $15.00 / 1M chars |
| `grok-stt-batch` | Speech-to-Text | — | $0.10 / hour |
| `grok-stt-streaming` | Speech-to-Text | — | $0.20 / hour |

**Supported Features:**
- **Ephemeral Tokens**: Secure, short-lived tokens for client-side voice sessions.
- **Custom Voices**: Support for creating and using unique voice profiles.

### Deprecated

The following models were retired on **May 15, 2026**, and are no longer recommended for new integrations.

| Model ID | Aliases | Inputs | Outputs | Context window | Knowledge cutoff | Retirement Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-2-1212` | `grok-2` | `text` | `text` | 131,072 | Aug 2024 | May 15, 2026 |
| `grok-2-vision-1212` | `grok-2-vision` | `text`, `image` | `text` | 131,072 | Aug 2024 | May 15, 2026 |
| `grok-beta` | — | `text` | `text` | 131,072 | — | May 15, 2026 |
| `grok-vision-beta` | — | `text`, `image` | `text` | 131,072 | — | May 15, 2026 |

## Notes

- **Real-time Data**: Grok does not have access to real-time events by default. Users must enable server-side search tools (`Web Search` or `X Search`) to incorporate live data into requests.
- **Prompt Caching**: xAI supports prompt caching to reduce costs and latency for repetitive context. Cached input tokens are typically billed at a discounted rate (refer to the API console for current percentages).
- **Batch API**: Asynchronous batch processing is available for non-latency-sensitive tasks, offering a significant discount (typically 50%) compared to standard inference.
- **Priority Processing**: A dedicated tier for high-throughput, low-latency requirements, ensuring consistent performance during peak usage.
- **Role Flexibility**: Chat models have no role order limitations; `system`, `user`, and `assistant` roles can be mixed in any sequence within the conversation context.
- **Vision Limits**: Maximum image size is 20MiB per file. There is no hard limit on the number of images per request. Supported formats include `jpg`, `jpeg`, and `png`.
- **Logprobs**: `logprobs` and `top_logprobs` are not supported for models `grok-4.20` and newer; these fields are silently ignored if provided in the request.
- **Rate Limits**: xAI uses a tiered system based on account balance and usage history. Tiers range from Tier 1 (Trial/Low) to Tier 5 (Enterprise), with increasing RPM (Requests Per Minute) and TPM (Tokens Per Minute) caps. Specific limits are visible in the xAI API Console.
- **Data Privacy**: xAI provides options for enterprise deployments with strict data residency and privacy controls. By default, API data is not used to train flagship models unless explicitly opted-in.
