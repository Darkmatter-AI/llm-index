---
provider: Google
slug: google
last_updated: 2026-06-22T08:17:54Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-06-22T08:17:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Gemini 3 Series
The latest generation of multimodal models, featuring frontier intelligence, superior search grounding, and native "thinking" capabilities.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-flash` | `gemini-3.5-flash-latest`, `gemini-3.5-flash-001` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multimodal | Standard, Batch, Flex, Priority | **Standard**: $1.50 input / $9.00 output<br>**Batch**: $0.75 input / $4.50 output<br>**Flex**: $0.75 input / $4.50 output<br>**Priority**: $2.70 input / $16.20 output |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-latest`, `gemini-3.1-pro-preview-customtools` | text, image, audio, video, PDF | text | 2,097,152 | 8,192 | — | Preview | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multimodal, vibe-coding | Standard, Batch, Flex, Priority | **Standard**: $2.00 (<=200k) / $4.00 (>200k) input; $12.00 (<=200k) / $18.00 (>200k) output<br>**Batch/Flex**: $1.00 (<=200k) / $2.00 (>200k) input; $6.00 (<=200k) / $9.00 (>200k) output<br>**Priority**: $3.60 (<=200k) / $7.20 (>200k) input; $21.60 (<=200k) / $32.40 (>200k) output |
| `gemini-3.1-flash-lite` | `gemini-3.1-flash-lite-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multimodal | Standard, Batch, Flex, Priority | **Standard**: $0.25 input ($0.50 audio) / $1.50 output<br>**Batch/Flex**: $0.125 input ($0.25 audio) / $0.75 output<br>**Priority**: $0.45 input ($0.90 audio) / $2.70 output |
| `gemini-3-flash-preview` | `gemini-3-flash-preview-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Preview | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multimodal | Standard, Batch, Flex, Priority | **Standard**: $0.50 input ($1.00 audio) / $3.00 output<br>**Batch/Flex**: $0.25 input ($0.50 audio) / $1.50 output<br>**Priority**: $0.90 input ($1.80 audio) / $5.40 output |

### Gemini 2.5 Series
High-performance multimodal models optimized for reasoning, coding, and high-volume tasks.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | `gemini-2.5-pro-latest`, `gemini-2.5-pro-001` | text, image, audio, video, PDF | text | 2,097,152 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, multimodal | Standard, Batch, Flex, Priority | **Standard**: $1.25 (<=200k) / $2.50 (>200k) input; $10.00 (<=200k) / $15.00 (>200k) output<br>**Batch/Flex**: $0.625 (<=200k) / $1.25 (>200k) input; $5.00 (<=200k) / $7.50 (>200k) output<br>**Priority**: $2.25 (<=200k) / $4.50 (>200k) input; $18.00 (<=200k) / $27.00 (>200k) output |
| `gemini-2.5-flash` | `gemini-2.5-flash-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multimodal | Standard, Batch, Flex, Priority | **Standard**: $0.30 input ($1.00 audio) / $2.50 output<br>**Batch/Flex**: $0.15 input ($0.50 audio) / $1.25 output<br>**Priority**: $0.54 input ($1.80 audio) / $4.50 output |
| `gemini-2.5-flash-lite` | `gemini-2.5-flash-lite-latest` | text, image, audio, video, PDF | text | 1,048,576 | 8,192 | — | Stable | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, multimodal | Standard | **Standard**: $0.10 input / $0.40 output |

### Audio & Realtime
Models optimized for low-latency speech-to-speech, text-to-speech, and live multimodal interaction.

| Model ID | Direction | Inputs | Outputs | Context Window | Release Stage | Capabilities | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | Speech-to-Speech | audio | audio | — | Preview | live API, 70+ languages, real-time translation | $3.50/MTok input ($0.0053/min)<br>$21.00/MTok output ($0.0315/min) |
| `gemini-3.1-flash-live-preview` | Multimodal Live | text, audio, image, video | text, audio | — | Preview | live API, acoustic nuance detection, multimodal awareness | **Input**: $0.75/MTok (text), $3.00/MTok (audio), $1.00/MTok (image/video)<br>**Output**: $4.50/MTok (text), $12.00/MTok (audio) |
| `gemini-3.1-flash-tts-preview` | Text-to-Speech | text | audio | — | Preview | steerable prompts, expressive audio tags | **Standard**: $1.00/MTok input / $20.00/MTok output<br>**Batch**: $0.50/MTok input / $10.00/MTok output |
| `gemini-2.5-flash-live-preview` | Multimodal Live | text, audio, image, video | text, audio | — | Preview | live API, sub-second native audio streaming | See `gemini-3.1-flash-live-preview` pricing |
| `gemini-2.5-flash-tts-preview` | Text-to-Speech | text | audio | — | Preview | controllable style and pacing | See `gemini-3.1-flash-tts-preview` pricing |
| `gemini-2.5-pro-tts-preview` | Text-to-Speech | text | audio | — | Preview | high-fidelity, optimized for podcasts/audiobooks | **Standard**: $2.50/MTok input / $50.00/MTok output |

### Generative Media
Models for high-efficiency image and video generation.

#### Image Generation

| Model ID | Inputs | Output Resolution | Release Stage | Price |
| :--- | :--- | :--- | :--- | :--- |
| `nano-banana-2` | text, image | Up to 4K | Stable | **Standard**: $60.00/MTok output (~$0.067/1K image)<br>**Batch**: $30.00/MTok output (~$0.034/1K image) |
| `nano-banana-pro` | text, image | Up to 4K | Stable | **Standard**: $120.00/MTok output (~$0.134/1K image)<br>**Batch**: $60.00/MTok output (~$0.067/1K image) |
| `gemini-3.1-flash-image` | text, image | Up to 4K | Stable | **Standard**: $60.00/MTok output (~$0.067/1K image)<br>**Batch**: $30.00/MTok output (~$0.034/1K image) |
| `gemini-3-pro-image` | text, image | Up to 4K | Stable | **Standard**: $120.00/MTok output (~$0.134/1K image)<br>**Batch**: $60.00/MTok output (~$0.067/1K image) |

#### Video Generation

| Model ID | Max Duration | Resolutions | Release Stage | Price |
| :--- | :--- | :--- | :--- | :--- |
| `veo-3.1-preview` | — | Cinematic, 4K | Preview | $0.15 per second |
| `veo-3.1-lite-preview` | — | Cinematic | Preview | $0.05 per second |

### Specialized & Agents
Models designed for autonomous research, UI automation, and robotics.

| Model ID | Function | Release Stage | Pricing |
| :--- | :--- | :--- | :--- |
| `gemini-deep-research-preview` | Autonomous multi-step research | Preview | $0.50 per research session |
| `gemini-deep-research-max-preview` | Maximum comprehensiveness research | Preview | $2.00 per research session |
| `antigravity-agent-preview` | Managed agent in Linux sandbox | Preview | $0.05 per minute of execution |
| `gemini-2.5-computer-use-preview` | UI automation (click, type, navigate) | Preview | Same as `gemini-2.5-flash` |
| `gemini-robotics-er-1.6-preview` | Embodied reasoning for robotics | Preview | — |

### Embeddings

| Model ID | Dimensions | Max Input | Modalities | Price (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2` | 768 (reducible) | 8,192 | text, image, audio, video, PDF | $0.10 |
| `gemini-embedding` | 768 | 3,072 | text | $0.10 |

### Deprecated

| Model ID | Shutdown Date | Replacement |
| :--- | :--- | :--- |
| `gemini-2.0-flash` | Shut down | `gemini-3.5-flash` |
| `gemini-2.0-flash-lite` | Shut down | `gemini-3.1-flash-lite` |
| `gemini-3.1-flash-lite-preview` | Shut down | `gemini-3.1-flash-lite` |
| `gemini-3-pro-preview` | Shut down | `gemini-3.1-pro-preview` |
| `imagen-4` | Deprecated | `nano-banana-2` |

## Notes

- **Free Tier**: Available for most models with generous limits (e.g., 15 RPM, 1M TPM). Content submitted in the Free Tier is used by Google to improve products.
- **Paid Tier**: Content is not used to improve products. Access to higher rate limits, Context Caching, and Batch API.
- **Batch API**: Offers a 50% cost reduction compared to Standard pricing for asynchronous tasks.
- **Context Caching**: Available in Paid Tier. Storage is billed at $1.00 per 1M tokens per hour (Standard) or $4.50 per 1M tokens per hour (Pro). Cached input tokens are billed at a 75% discount (25% of the standard input price).
- **Grounding**: Grounding with Google Search and Google Maps is billed per 1,000 queries. Gemini 3 models include 5,000 free shared prompts per month, then $14 per 1,000 queries. Gemini 2.5 Pro is $35 per 1,000 search queries.
- **Thinking Tokens**: For models with "thinking" capabilities, the output price includes the tokens generated during the thinking process.
- **Rate Limits**:
    - **Flash Models (Paid)**: 2,000 RPM / 4M TPM.
    - **Pro Models (Paid)**: 1,000 RPM / 2M TPM.
    - **Free Tier**: Typically 2-15 RPM and 1,500 RPD depending on the model.
- **Data Residency**: Options available via Vertex AI integration; Gemini API (AI Studio) primarily operates in US-central regions with global availability.
