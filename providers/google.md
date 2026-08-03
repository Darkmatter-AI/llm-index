---
provider: Google
slug: google
last_updated: 2026-08-03T09:55:07Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-08-03T09:55:07Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Gemini 3 Series (Latest)
The Gemini 3 generation represents the frontier of Google's multimodal intelligence, featuring integrated "thinking" capabilities, superior agentic performance, and native grounding with Google Search and Maps.

| Model ID | Aliases | Inputs | Outputs | Context Window | Max Output | Cutoff | Stage | Capabilities | Latency / SLA |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.6-flash` | `gemini-3.6-flash-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking | Standard, Flex, Priority, Batch |
| `gemini-3.5-flash` | `gemini-3.5-flash-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking | Standard, Flex, Priority, Batch |
| `gemini-3.5-flash-lite` | `gemini-3.5-flash-lite-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking | Standard, Flex, Priority, Batch |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-customtools` | text, image, audio, video, PDF | text | 2,097,152 | 8,192 | — | Preview | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking | Standard, Flex, Priority, Batch |
| `gemini-3.1-flash-lite` | `gemini-3.1-flash-lite-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps | Standard, Flex, Priority, Batch |
| `gemini-3-flash-preview` | `gemini-3-flash-preview-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Preview | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps | Standard, Flex, Priority, Batch |

#### Gemini 3 Pricing (USD per 1M tokens)

| Model ID | Tier | Input | Output (incl. thinking) | Context Caching (Storage) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-3.6-flash` | Standard | $1.50 | $7.50 | $0.15 ($1.00/1M/hr) |
| | Flex / Batch | $0.75 | $3.75 | $0.075 ($1.00/1M/hr) |
| | Priority | $2.70 | $13.50 | $0.27 ($1.00/1M/hr) |
| `gemini-3.5-flash` | Standard | $1.50 | $9.00 | $0.15 ($1.00/1M/hr) |
| | Flex / Batch | $0.75 | $4.50 | $0.075 ($1.00/1M/hr) |
| | Priority | $2.70 | $16.20 | $0.27 ($1.00/1M/hr) |
| `gemini-3.5-flash-lite` | Standard | $0.30 | $2.50 | $0.03 ($1.00/1M/hr) |
| | Flex / Batch | $0.15 | $1.25 | $0.02 ($1.00/1M/hr) |
| | Priority | $0.54 | $4.50 | $0.05 ($1.00/1M/hr) |
| `gemini-3.1-pro-preview` | Standard (<=200k) | $2.00 | $12.00 | $0.20 ($4.50/1M/hr) |
| | Standard (>200k) | $4.00 | $18.00 | $0.40 ($4.50/1M/hr) |
| | Flex / Batch (<=200k) | $1.00 | $6.00 | $0.20 ($4.50/1M/hr) |
| | Priority (<=200k) | $3.60 | $21.60 | $0.36 ($8.10/1M/hr) |
| `gemini-3.1-flash-lite` | Standard | $0.25 | $1.50 | $0.025 ($1.00/1M/hr) |
| | Flex / Batch | $0.125 | $0.75 | $0.0125 ($0.50/1M/hr) |

### Gemini 2.5 Series
The Gemini 2.5 generation provides a stable, high-performance baseline for production applications with established pricing tiers.

| Model ID | Aliases | Inputs | Outputs | Context Window | Max Output | Cutoff | Stage | Capabilities | Latency / SLA |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | `gemini-2.5-pro-latest` | text, image, audio, video, PDF | text | 2,097,152 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution | Standard, Batch |
| `gemini-2.5-flash` | `gemini-2.5-flash-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution | Standard, Batch |
| `gemini-2.5-flash-lite` | `gemini-2.5-flash-lite-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution | Standard, Batch |

#### Gemini 2.5 Pricing (USD per 1M tokens)

| Model ID | Tier | Input | Output | Context Caching (Storage) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | Standard (<=128k) | $1.25 | $3.75 | $0.3125 ($4.50/1M/hr) |
| | Standard (>128k) | $2.50 | $7.50 | $0.625 ($4.50/1M/hr) |
| `gemini-2.5-flash` | Standard (<=128k) | $0.075 | $0.30 | $0.01875 ($1.00/1M/hr) |
| | Standard (>128k) | $0.15 | $0.60 | $0.0375 ($1.00/1M/hr) |

### Realtime & Audio
Models optimized for the Live API, real-time dialogue, and speech-to-speech translation.

| Model ID | Direction | Inputs | Outputs | Stage | Pricing (Input) | Pricing (Output) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | Speech-to-Speech | audio | audio | Preview | $3.50 / 1M tokens ($0.0053/min) | $21.00 / 1M tokens ($0.0315/min) |
| `gemini-3.1-flash-live-preview` | Multimodal Live | text, audio, image, video | text, audio | Preview | $0.75 (text) / $3.00 (audio) / $1.00 (media) | $4.50 (text) / $12.00 (audio) |
| `gemini-3.1-flash-tts-preview` | Text-to-Speech | text | audio | Preview | $1.00 / 1M tokens | $20.00 / 1M tokens |
| `gemini-2.5-flash-live-preview` | Multimodal Live | text, audio, image, video | text, audio | Preview | $0.075 (text) / $0.30 (audio) | $0.30 (text) / $1.20 (audio) |

### Image & Video Generation
Google's generative media models, including the Nano Banana and Veo families.

| Model ID | Category | Inputs | Output Resolution | Price per 1M Output Tokens | Effective Price |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-flash-image` | Image (Nano Banana 2) | text, image | Up to 4K | $60.00 | $0.067 (1K) / $0.151 (4K) |
| `gemini-3.1-flash-lite-image` | Image (Nano Banana 2 Lite) | text, image | Up to 1K | $30.00 | $0.0336 (1K) |
| `gemini-omni-flash-preview` | Video | text, image | 720p | $17.50 | ~$0.10 per second |
| `veo-3.1-preview` | Video | text, image | Up to 4K | — | — |
| `nano-banana-pro` | Image | text, image | 4K | — | — |

### Embeddings
Multimodal and text-only embedding models for RAG and semantic search.

| Model ID | Dimensions | Max Input | Modalities | Price per 1M Tokens |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2` | — | — | text, image, video, audio, PDF | $0.10 (text) / $0.20 (media) |
| `text-embedding-004` | 768 (reducible) | 2,048 | text | $0.10 |

### Specialized & Agentic
Models designed for specific UI automation, research, or robotics tasks.

| Model ID | Function | Pricing |
| :--- | :--- | :--- |
| `computer-use-preview` | UI automation (click, type, navigate) | Billed at `gemini-2.5-flash` rates |
| `gemini-deep-research-preview` | Autonomous multi-step research | Billed per research task / agent hour |
| `gemini-robotics-er-2-preview` | Embodied reasoning for robotics | Billed per streaming session |

### Deprecated
Models scheduled for shutdown. Migrate to Gemini 3.x or 2.5.x.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `gemini-2.0-flash` | Shut down | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | Shut down | `gemini-3.5-flash-lite` |
| `gemini-3.1-flash-lite-preview` | Shut down | `gemini-3.1-flash-lite` |
| `gemini-3-pro-preview` | Shut down | `gemini-3.1-pro-preview` |
| `imagen-4` | Deprecated | `nano-banana-2` |

## Notes

- **Free Tier**: Available for most models in Google AI Studio. Content submitted via the free tier is used to improve Google products. Rate limits are typically 15 RPM, 1M TPM, and 1,500 RPD.
- **Paid Tier**: Content is not used for training. Supports higher rate limits and access to advanced features like Context Caching and Batch API.
- **Batch API**: Offers a 50% discount on standard input and output token prices. Requests are processed within 24 hours.
- **Context Caching**: Billed in two parts: a one-time processing fee ($/1M tokens) and a recurring storage fee ($/1M tokens per hour). Storage is billed until the cache is deleted.
- **Grounding**: Grounding with Google Search is charged at $14 per 1,000 search queries after a 5,000-query monthly free allowance (shared across Gemini 3.x models).
- **Rate Limit Tiers**: Pay-as-you-go users are grouped into Tiers 1-5 based on payment history and usage. Tier 1 typically starts at 2,000 RPM and 4M TPM for Flash models.
- **Thinking Tokens**: For Gemini 3.x models, "thinking" tokens generated during reasoning are billed at the same rate as standard output tokens.
- **Regional Availability**: Gemini API is available in 200+ countries and territories. Data residency options are available via Vertex AI (Google Cloud).
