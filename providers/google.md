---
provider: Google
slug: google
last_updated: 2026-05-19T11:37:42Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-05-19T11:37:42Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Gemini 3.x Series (Chat / Reasoning)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-customtools`, `gemini-pro-latest` | text, image, audio, video, PDF, code | text | 2,000,000 | 8,192 | Preview | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, grounding with Google Search, grounding with Google Maps, custom tools |
| `gemini-3.1-flash-lite` | `gemini-3.1-flash-lite-preview`, `gemini-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, grounding with Google Search, grounding with Google Maps |
| `gemini-3-flash-preview` | — | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | Preview | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, grounding with Google Search, grounding with Google Maps |

| Model ID | Latency Tier | Pricing (Input / MTok) | Pricing (Cached / MTok) | Pricing (Output / MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-pro-preview` | Standard, Batch, Flex, Priority | $2.00 (≤200k)<br>$4.00 (>200k) | $0.20 (≤200k)<br>$0.40 (>200k) | $12.00 (≤200k)<br>$18.00 (>200k) |
| `gemini-3.1-flash-lite` | Standard, Batch, Flex, Priority | $0.25 (text/img/vid)<br>$0.50 (audio) | $0.025 (text/img/vid)<br>$0.05 (audio) | $1.50 |
| `gemini-3-flash-preview` | Standard, Batch, Flex, Priority | $0.50 (text/img/vid)<br>$1.00 (audio) | $0.05 (text/img/vid)<br>$0.10 (audio) | $3.00 |

### Gemini 2.5 Series (Chat / Reasoning)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | — | text, image, audio, video, PDF, code | text | 2,000,000 | 8,192 | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, grounding with Google Search, grounding with Google Maps |
| `gemini-2.5-flash` | — | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, grounding with Google Search, grounding with Google Maps, thinking budgets |
| `gemini-2.5-flash-lite` | `gemini-2.5-flash-lite-preview-09-2025` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, grounding with Google Search, grounding with Google Maps |

| Model ID | Latency Tier | Pricing (Input / MTok) | Pricing (Cached / MTok) | Pricing (Output / MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | Standard, Batch, Flex, Priority | $1.25 (≤200k)<br>$2.50 (>200k) | $0.125 (≤200k)<br>$0.25 (>200k) | $10.00 (≤200k)<br>$15.00 (>200k) |
| `gemini-2.5-flash` | Standard, Batch, Flex, Priority | $0.30 (text/img/vid)<br>$1.00 (audio) | $0.03 (text/img/vid)<br>$0.10 (audio) | $2.50 |
| `gemini-2.5-flash-lite` | Standard, Batch, Flex, Priority | $0.10 (text/img/vid)<br>$0.30 (audio) | $0.01 (text/img/vid)<br>$0.03 (audio) | $0.40 |

### Realtime & Audio

| Model ID | Direction | Inputs | Outputs | Release Stage | Capabilities | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-flash-live-preview` | Multimodal | text, audio, image, video | text, audio | Preview | Live API, real-time dialogue, acoustic nuance detection | Input: $0.75/MTok (text), $3.00/MTok (audio), $1.00/MTok (img/vid)<br>Output: $4.50/MTok (text), $12.00/MTok (audio) |
| `gemini-3.1-flash-tts-preview` | TTS | text | audio | Preview | controllable speech generation, expressive audio tags | Input: $1.00/MTok (text)<br>Output: $20.00/MTok (audio) |
| `gemini-2.5-flash-native-audio-preview-12-2025` | Multimodal | text, audio, video | text, audio | Preview | Live API, native audio reasoning | Input: $0.50/MTok (text), $3.00/MTok (audio/vid)<br>Output: $2.00/MTok (text), $12.00/MTok (audio) |
| `gemini-2.5-flash-preview-tts` | TTS | text | audio | Preview | controllable text-to-speech | Input: $0.50/MTok (text)<br>Output: $10.00/MTok (audio) |
| `gemini-2.5-pro-preview-tts` | TTS | text | audio | Preview | high-fidelity speech synthesis | Input: $1.00/MTok (text)<br>Output: $20.00/MTok (audio) |

### Image Generation

| Model ID | Inputs | Output Resolution | Release Stage | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `imagen-4.0-fast-generate-001` | text | Up to 2K | Preview | $0.02 per image |
| `imagen-4.0-generate-001` | text | Up to 2K | Preview | $0.04 per image |
| `imagen-4.0-ultra-generate-001` | text | Up to 2K | Preview | $0.06 per image |
| `gemini-3.1-flash-image-preview` | text, image | Up to 4K | Preview | Input: $0.50/MTok<br>Output: $60.00/MTok (~$0.045-$0.151/img) |
| `gemini-3-pro-image-preview` | text, image | Up to 4K | Preview | Input: $2.00/MTok (~$0.0011/img)<br>Output: $120.00/MTok (~$0.134-$0.24/img) |
| `gemini-2.5-flash-image` | text, image | Up to 1K | Preview | Input: $0.30/MTok<br>Output: $30.00/MTok (~$0.039/img) |

### Video & Music Generation

| Model ID | Category | Max Duration | Resolution | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `veo-3.1-generate-preview` | Video | — | 720p, 1080p, 4K | $0.40/sec (720p/1080p), $0.60/sec (4K) |
| `veo-3.1-fast-generate-preview` | Video | — | 720p, 1080p, 4K | $0.10/sec (720p), $0.12/sec (1080p), $0.30/sec (4K) |
| `veo-3.1-lite-generate-preview` | Video | — | 720p, 1080p | $0.05/sec (720p), $0.08/sec (1080p) |
| `veo-3.0-generate-001` | Video | — | — | $0.40/sec |
| `veo-2.0-generate-001` | Video | — | — | $0.35/sec |
| `lyria-3-pro-preview` | Music | Full Song | — | $0.08 per song |
| `lyria-3-clip-preview` | Music | 30s | — | $0.04 per song |

### Embeddings & Specialized

| Model ID | Description | Inputs | Max Input | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2` | Multimodal embedding model | text, image, video, audio, PDF | — | Text: $0.20/MTok, Image: $0.45/MTok, Audio: $6.50/MTok, Video: $12.00/MTok |
| `gemini-embedding-001` | Text-only embedding model | text | — | $0.15/MTok |
| `gemini-2.5-computer-use-preview-10-2025` | Browser control and UI automation | text, image | — | Input: $1.25/MTok (≤200k), $2.50/MTok (>200k)<br>Output: $10.00/MTok (≤200k), $15.00/MTok (>200k) |
| `gemini-robotics-er-1.6-preview` | Embodied reasoning for robotics | text, image, video, audio | — | Input: $1.00/MTok (text/img/vid), $2.00/MTok (audio)<br>Output: $5.00/MTok |
| `gemini-deep-research-preview` | Agentic multi-step research | text, web | — | Standard Gemini list rates + tool fees |

### Deprecated

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `gemini-3-pro-preview` | March 9, 2026 (Shut down) | `gemini-3.1-pro-preview` |
| `gemini-2.0-flash` | June 1, 2026 | `gemini-2.5-flash` |
| `gemini-2.0-flash-lite` | June 1, 2026 | `gemini-2.5-flash-lite` |

## Notes

- **Batch Discount**: All models supported by the Batch API receive a 50% cost reduction compared to standard rates.
- **Free Tier**: Available for developers and small projects. Content submitted via the free tier may be used by Google to improve products. Content in the Paid tier is not used for training.
- **Context Caching**: Storage is billed at $1.00 to $8.10 per 1,000,000 tokens per hour depending on the model tier. Input tokens for cached content are billed at a significantly lower rate (approx. 10% of standard input).
- **Grounding Pricing**: 
    - Gemini 3 series: 5,000 prompts/month free, then $14 per 1,000 Google Search queries.
    - Gemini 2.5 series: 1,500 RPD free, then $35 per 1,000 grounded prompts for Search and $25 per 1,000 for Maps.
- **Modality Billing**: PDF documents are billed at the image token rate. Audio is billed at a rate corresponding to 25 tokens per second.
- **Thinking Tokens**: For models with reasoning capabilities (e.g., Gemini 2.5 Flash), thinking tokens are billed at the standard output token rate.
- **Rate Limits**: Free tier limits are typically 15 RPM / 1M TPM / 1,500 RPD for Flash models. Paid tier limits scale from Tier 1 to Tier 5 based on usage and payment history.
- **Regional Availability**: Google AI Studio usage is free in all available regions; Vertex AI offers regional data residency options for enterprise customers.
