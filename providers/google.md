---
provider: Google
slug: google
last_updated: 2026-08-10T07:49:39Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-08-10T07:49:39Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Gemini 3 (Latest)

The Gemini 3 series represents the latest generation of multimodal models, optimized for speed, agentic tasks, and long-context reasoning.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.6-flash` | `gemini-3.6-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | Input: $1.50<br>Output: $7.50 |
| `gemini-3.5-flash` | `gemini-3.5-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | Input: $1.50<br>Output: $9.00 |
| `gemini-3.5-flash-lite` | `gemini-3.5-flash-lite-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | Input: $0.30<br>Output: $2.50 |
| `gemini-3.1-flash-lite` | `gemini-3.1-flash-lite-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | Input: $0.25<br>Output: $1.50 |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-customtools` | text, image, audio, video, PDF, code | text | 2,097,152 | 8,192 | — | Preview | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context, thinking | Standard, Batch, Flex, Priority | **Standard (<=200k)**: $2.00 / $12.00<br>**Standard (>200k)**: $4.00 / $18.00<br>**Priority (<=200k)**: $3.60 / $21.60<br>**Priority (>200k)**: $7.20 / $32.40 |
| `gemini-3-flash-preview` | `gemini-3-flash-preview-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Preview | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | Input: $0.50<br>Output: $3.00 |

### Gemini 2.5 (Current)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | `gemini-2.5-pro-latest` | text, image, audio, video, PDF, code | text | 2,097,152 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | — |
| `gemini-2.5-flash` | `gemini-2.5-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | — |
| `gemini-2.5-flash-lite` | `gemini-2.5-flash-lite-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, Maps grounding, URL context | Standard, Batch, Flex, Priority | — |

### Realtime & Audio

Models optimized for low-latency speech-to-speech, text-to-speech, and live multimodal interactions.

| Model ID | Inputs | Outputs | Release Stage | Languages | Capabilities | Pricing (per 1M tokens / min) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | audio | audio | Preview | 70+ | live API, translation | Input: $3.50 ($0.0053/min)<br>Output: $21.00 ($0.0315/min) |
| `gemini-3.1-flash-live-preview` | text, image, audio, video | text, audio | Preview | — | live API, multimodal awareness | Text: $0.75 / $4.50<br>Audio: $3.00 / $12.00<br>Image/Video: $1.00 / — |
| `gemini-3.1-flash-tts-preview` | text | audio | Preview | — | speech generation, expressive audio tags | Input: $1.00<br>Output: $20.00 |
| `gemini-omni-flash` | text, image, audio, video | text, video | Preview | — | video generation, video editing | Text: $1.50 / $9.00<br>Video: — / $17.50 |
| `gemini-2.5-flash-native-audio-preview-12-2025` | audio | audio | Preview | — | live API, native audio reasoning | — |
| `gemini-2.5-flash-preview-tts` | text | audio | Preview | — | controllable text-to-speech | — |
| `gemini-2.5-pro-preview-tts` | text | audio | Preview | — | high-fidelity speech synthesis | — |

### Image Generation (Nano Banana)

| Model ID | Inputs | Output Resolution | Price per Image | Price per MTok (Output) | Batch Discount |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-flash-image` | text, image | 0.5K, 1K, 2K, 4K | $0.045 (0.5K), $0.067 (1K), $0.101 (2K), $0.151 (4K) | $60.00 | 50% |
| `gemini-3.1-flash-lite-image` | text, image, video | 1K | $0.0336 (1K) | $30.00 | 50% |
| `gemini-3-pro-image` | text, image | 4K | — | — | — |
| `gemini-2.5-flash-image` | text, image | — | — | — | — |

### Video Generation (Veo)

| Model ID | Release Stage | Capabilities | Audio |
| :--- | :--- | :--- | :--- |
| `veo-3.1-generate-preview` | Preview | cinematic video generation, creative controls | Natively synchronized |
| `veo-3.1-lite-generate-preview` | Preview | high-efficiency video generation | — |

### Embeddings

| Model ID | Output Dimensions | Max Input Tokens | Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2-preview` | — | — | text, image, video, audio, PDF | — |
| `text-embedding-004` | 768 (Matryoshka) | 3,072 | text | $0.10 |
| `embedding-001` | 768 | 3,072 | text | $0.10 |

### Specialized

| Model ID | Function | Pricing |
| :--- | :--- | :--- |
| `gemini-2.5-computer-use-preview-10-2025` | UI automation (clicking, typing, navigating) | — |
| `deep-research-preview-04-2026` | Agentic multi-step research across hundreds of sources | — |
| `deep-research-max-preview-04-2026` | Maximum comprehensiveness automated context gathering | — |
| `antigravity-preview-05-2026` | Managed agent in isolated Linux sandbox | — |
| `gemini-robotics-er-2-preview` | Embodied reasoning and multi-robot collaboration | — |
| `gemini-robotics-er-1.6-preview` | Spatial reasoning and task planning for robotics | — |

### Deprecated

| Model ID | Status | Shutdown Date |
| :--- | :--- | :--- |
| `gemini-2.0-flash` | Shut down | — |
| `gemini-2.0-flash-lite` | Shut down | — |
| `gemini-3.1-flash-lite-preview` | Shut down | — |
| `gemini-3-pro-preview` | Shut down | — |
| `imagen-4.0-generate` | Deprecated | — |

## Notes

- **Batch Discount**: All models support a Batch API with a **50% cost reduction** compared to standard pricing.
- **Context Caching**: Available on the Paid tier. Pricing consists of a retrieval cost (e.g., $0.15/MTok for Gemini 3.6 Flash) and a storage cost of **$1.00 per 1M tokens per hour**.
- **Free Tier**: Offers generous limits (e.g., 15 RPM / 1M TPM for Flash-class models). Content submitted via the Free tier **is used to improve Google products**.
- **Grounding**: Supports "Grounding with Google Search" and "Grounding with Google Maps". Includes 5,000 free search requests per month (shared across Gemini 3.x), then **$14 per 1,000 requests**.
- **Rate Limit Tiers**:
    - **Free**: 2 RPM / 32k TPM / 50 RPD (Pro); 15 RPM / 1M TPM / 1500 RPD (Flash).
    - **Paid (Tier 1)**: 5 RPM / 10M TPM (Pro); 2000 RPM / 4M TPM (Flash).
- **Data Residency**: Content in the Paid and Enterprise tiers is **not used to improve Google products** and supports regional data residency options.
- **Thinking Tokens**: For models with "thinking" capabilities (e.g., Gemini 3.1 Pro), output pricing includes the tokens generated during the internal reasoning process.
- **Audio Billing**: Audio tokens are calculated at a rate of **25 tokens per second** of audio.
- **Video Billing**: Video output (e.g., Gemini Omni Flash) is billed at **5,792 tokens per second** of 720p video, equating to ~$0.10/sec under standard pricing.
