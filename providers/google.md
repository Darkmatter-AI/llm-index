---
provider: Google
slug: google
last_updated: 2026-05-18T17:31:04Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-05-18T17:31:04Z`

## Models

### Gemini

| Model | Tier | Input | Output | Capabilities |
| --- | --- | --- | --- | --- |
| `gemini-3.1-pro-preview` | ≤200k tokens | $2.00 / 1M tokens | $12.00 / 1M tokens | vision, tools, reasoning |
| `gemini-3.1-pro-preview` | >200k tokens | $4.00 / 1M tokens | $18.00 / 1M tokens | vision, tools, reasoning |
| `gemini-3-flash-preview` | Text/Image/Video | $0.50 / 1M tokens | $3.00 / 1M tokens | vision, tools, reasoning |
| `gemini-3-flash-preview` | Audio | $1.00 / 1M tokens | $3.00 / 1M tokens | audio, vision, tools, reasoning |
| `gemini-3.1-flash-lite` | Text/Image/Video | $0.25 / 1M tokens | $1.50 / 1M tokens | vision, tools |
| `gemini-3.1-flash-lite` | Audio | $0.50 / 1M tokens | $1.50 / 1M tokens | audio, vision, tools |
| `gemini-2.5-pro` | ≤200k tokens | $1.25 / 1M tokens | $10.00 / 1M tokens | vision, tools, reasoning, coding |
| `gemini-2.5-pro` | >200k tokens | $2.50 / 1M tokens | $15.00 / 1M tokens | vision, tools, reasoning, coding |
| `gemini-2.5-flash` | Text/Image/Video | $0.30 / 1M tokens | $2.50 / 1M tokens | vision, tools, reasoning |
| `gemini-2.5-flash` | Audio | $1.00 / 1M tokens | $2.50 / 1M tokens | audio, vision, tools, reasoning |
| `gemini-2.5-flash-lite` | Text/Image/Video | $0.10 / 1M tokens | $0.40 / 1M tokens | vision, tools |
| `gemini-2.5-flash-lite` | Audio | $0.30 / 1M tokens | $0.40 / 1M tokens | audio, vision, tools |
| `gemini-2.0-flash` | Text/Image/Video | $0.10 / 1M tokens | $0.40 / 1M tokens | vision, tools |
| `gemini-2.0-flash` | Audio | $0.70 / 1M tokens | $0.40 / 1M tokens | audio, vision, tools |
| `gemini-2.0-flash-lite` | All Modalities | $0.075 / 1M tokens | $0.30 / 1M tokens | vision, tools |

### Image Generation

| Model | Input | Output |
| --- | --- | --- |
| `gemini-3-pro-image-preview` | $2.00 / 1M tokens (text/image) | $12.00 / 1M tokens (text), $120.00 / 1M tokens (images) |
| `gemini-3.1-flash-image-preview` | $0.50 / 1M tokens (text/image) | $3.00 / 1M tokens (text), $60.00 / 1M tokens (images) |
| `gemini-2.5-flash-image` | $0.30 / 1M tokens (text/image) | $0.039 / image |
| `imagen-4.0-fast-generate-001` | - | $0.02 / image |
| `imagen-4.0-generate-001` | - | $0.04 / image |
| `imagen-4.0-ultra-generate-001` | - | $0.06 / image |

### Video Generation

| Model | Quality | Price per Second |
| --- | --- | --- |
| `veo-3.1-lite-generate-preview` | 720p | $0.05 |
| `veo-3.1-lite-generate-preview` | 1080p | $0.08 |
| `veo-3.1-fast-generate-preview` | 720p | $0.10 |
| `veo-3.1-fast-generate-preview` | 1080p | $0.12 |
| `veo-3.1-fast-generate-preview` | 4K | $0.30 |
| `veo-3.1-generate-preview` | 720p/1080p | $0.40 |
| `veo-3.1-generate-preview` | 4K | $0.60 |
| `veo-3.0-fast-generate-001` | 720p | $0.10 |
| `veo-3.0-fast-generate-001` | 1080p | $0.12 |
| `veo-3.0-fast-generate-001` | 4K | $0.30 |
| `veo-3.0-generate-001` | All | $0.40 |
| `veo-2.0-generate-001` | All | $0.35 |

### Audio and Speech

| Model | Modality | Input | Output |
| --- | --- | --- | --- |
| `gemini-3.1-flash-live-preview` | Text | $0.75 / 1M tokens | $4.50 / 1M tokens |
| `gemini-3.1-flash-live-preview` | Audio | $3.00 / 1M tokens ($0.005/min) | $12.00 / 1M tokens ($0.018/min) |
| `gemini-3.1-flash-live-preview` | Image/Video | $1.00 / 1M tokens ($0.002/min) | - |
| `gemini-2.5-flash-native-audio-preview-12-2025` | Text | $0.50 / 1M tokens | $2.00 / 1M tokens |
| `gemini-2.5-flash-native-audio-preview-12-2025` | Audio/Video | $3.00 / 1M tokens | $12.00 / 1M tokens (audio) |
| `gemini-3.1-flash-tts-preview` | Text-to-Speech | $1.00 / 1M tokens | $20.00 / 1M tokens (audio) |
| `gemini-2.5-pro-preview-tts` | Text-to-Speech | $1.00 / 1M tokens | $20.00 / 1M tokens (audio) |
| `gemini-2.5-flash-preview-tts` | Text-to-Speech | $0.50 / 1M tokens | $10.00 / 1M tokens (audio) |

### Music Generation

| Model | Price per Request |
| --- | --- |
| `lyria-3-clip-preview` (30s) | $0.04 |
| `lyria-3-pro-preview` (Full Song) | $0.08 |

### Embeddings

| Model | Modality | Price per 1M Tokens |
| --- | --- | --- |
| `gemini-embedding-2` | Text | $0.20 |
| `gemini-embedding-2` | Image | $0.45 |
| `gemini-embedding-2` | Audio | $6.50 |
| `gemini-embedding-2` | Video | $12.00 |
| `gemini-embedding-001` | Text | $0.15 |

### Specialized Models

| Model | Tier | Input | Output |
| --- | --- | --- | --- |
| `gemini-2.5-computer-use-preview-10-2025` | ≤200k tokens | $1.25 / 1M tokens | $10.00 / 1M tokens |
| `gemini-2.5-computer-use-preview-10-2025` | >200k tokens | $2.50 / 1M tokens | $15.00 / 1M tokens |
| `gemini-robotics-er-1.6-preview` | Text/Image/Video | $1.00 / 1M tokens | $5.00 / 1M tokens |
| `gemini-robotics-er-1.6-preview` | Audio | $2.00 / 1M tokens | $5.00 / 1M tokens |

## Notes

- A free tier is available with limited access to certain models.
- The Batch API offers a 50% cost reduction on eligible models.
- Context caching is available on the paid tier for select models, with pricing for cached tokens and a per-hour storage fee.
- Deprecated models, such as `gemini-2.0-flash`, have scheduled shutdown dates. Users are advised to migrate to newer models to avoid service disruption.
- Tool usage, such as Google Search or Code Execution, is billed at its own rate in addition to the model's token consumption.
- Tokens for PDF and other document modalities are billed at the same rate as image tokens.
- Preview models may have more restrictive rate limits and can change before becoming stable.
