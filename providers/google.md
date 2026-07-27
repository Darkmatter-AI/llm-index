---
provider: Google
slug: google
last_updated: 2026-07-27T10:00:03Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-07-27T10:00:03Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Gemini 3 Series
The Gemini 3 series represents the latest generation of multimodal models, featuring integrated "thinking" capabilities and optimized performance for agentic workflows and high-speed reasoning.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Cutoff | Stage | Languages | Capabilities | Latency | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.6-flash` | `gemini-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multilingual | Fast | **Standard**: $1.50 / $7.50<br>**Batch/Flex**: $0.75 / $3.75<br>**Priority**: $2.70 / $13.50 |
| `gemini-3.5-flash` | — | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multilingual | Fast | **Standard**: $1.50 / $9.00<br>**Batch/Flex**: $0.75 / $4.50<br>**Priority**: $2.70 / $16.20 |
| `gemini-3.5-flash-lite` | — | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multilingual | Fastest | **Standard**: $0.30 / $2.50<br>**Batch/Flex**: $0.15 / $1.25<br>**Priority**: $0.54 / $4.50 |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-customtools` | text, image, audio, video, PDF, code | text | 2,097,152 | — | — | Preview | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multilingual | Moderate | **Standard (<=200k)**: $2.00 / $12.00<br>**Standard (>200k)**: $4.00 / $18.00<br>**Batch/Flex (<=200k)**: $1.00 / $6.00<br>**Batch/Flex (>200k)**: $2.00 / $9.00<br>**Priority (<=200k)**: $3.60 / $21.60<br>**Priority (>200k)**: $7.20 / $32.40 |
| `gemini-3.1-flash-lite` | — | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multilingual | Fastest | **Standard**: $0.25 / $1.50<br>**Batch/Flex**: $0.125 / $0.75<br>**Priority**: $0.45 / $2.70 |
| `gemini-3-flash-preview` | — | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Preview | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, thinking, multilingual | Fast | **Standard**: $0.50 / $3.00<br>**Batch/Flex**: $0.25 / $1.50<br>**Priority**: $0.90 / $5.40 |

### Gemini 2.5 Series
The 2.5 series serves as the stable workhorse generation for production applications requiring high reliability and established reasoning patterns.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Cutoff | Stage | Languages | Capabilities | Latency | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | `gemini-pro-latest`, `gemini-2.5-pro-001` | text, image, audio, video, PDF, code | text | 2,097,152 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, multilingual | Moderate | — |
| `gemini-2.5-flash` | `gemini-2.5-flash-001` | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, multilingual | Fast | — |
| `gemini-2.5-flash-lite` | — | text, image, audio, video, PDF, code | text | 1,048,576 | — | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, multilingual | Fastest | — |

### Realtime & Audio
Models optimized for the Live API, low-latency speech-to-speech, and high-fidelity text-to-speech.

| Model ID | Direction | Inputs | Outputs | Stage | Languages | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | Speech-to-Speech | audio | audio | Preview | 70+ | **Input**: $3.50/MTok (~$0.0053/min)<br>**Output**: $21.00/MTok (~$0.0315/min) |
| `gemini-3.1-flash-live-preview` | Multimodal Live | text, image, audio, video | text, audio | Preview | — | **Input**: $0.75 (text), $3.00 (audio), $1.00 (media) / MTok<br>**Output**: $4.50 (text), $12.00 (audio) / MTok |
| `gemini-3.1-flash-tts-preview` | Text-to-Speech | text | audio | Preview | — | **Input**: $1.00/MTok<br>**Output**: $20.00/MTok (25 tokens/sec) |
| `gemini-2.5-flash-live-preview` | Multimodal Live | text, image, audio, video | text, audio | Preview | — | — |

### Image Generation
Google's native image generation models, branded as Nano Banana, optimized for speed and contextual reasoning.

| Model ID | Aliases | Inputs | Output Resolution | Price per Image (1K) | Price per MTok |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-flash-image` | `nano-banana-2` | text, image | 512px to 4096px | $0.067 | $60.00 (Output) |
| `gemini-3.1-flash-lite-image` | `nano-banana-2-lite` | text, image | 1024x1024 | $0.0336 | $30.00 (Output) |
| `gemini-3-pro-image` | `nano-banana-pro` | text, image | Up to 4K | — | — |
| `gemini-2.5-flash-image` | `nano-banana` | text, image | — | — | — |

### Video Generation
Cinematic and conversational video generation models.

| Model ID | Max Duration | Supported Resolutions | Price per Second | Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| `veo-3.1-preview` | — | Cinematic | — | Advanced creative controls, synced audio |
| `veo-3.1-lite-preview` | — | Cinematic | — | High-efficiency, developer-first |
| `gemini-omni-flash-preview` | — | 720p | ~$0.10 | Conversational video editing, text/image to video |

### Embeddings
Unified multimodal embedding models for semantic search and RAG.

| Model ID | Dimensions | Max Input | Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2` | — | — | text, image, video, audio, PDF | — |
| `text-embedding-004` | 768 (reducible) | 2,048 | text | $0.10 |

### Specialized & Agents
Models designed for autonomous planning, research, and UI automation.

| Model ID | Description | Pricing |
| :--- | :--- | :--- |
| `computer-use-preview` | Specialized model for UI actions (clicking, typing, navigating) | — |
| `gemini-deep-research-preview` | Autonomous research agent for multi-step planning and synthesis | — |
| `antigravity-agent-preview` | Managed agent running code and browsing in isolated Linux sandboxes | — |
| `gemini-robotics-er-1.6-preview` | Embodied reasoning for physical spaces and robotic task planning | — |

### Deprecated
Models scheduled for shutdown or replaced by newer generations.

| Model ID | Shutdown Date | Replacement |
| :--- | :--- | :--- |
| `gemini-2.0-flash` | Shut down | `gemini-2.5-flash` |
| `gemini-2.0-flash-lite` | Shut down | `gemini-2.5-flash-lite` |
| `gemini-3.1-flash-lite-preview` | Shut down | `gemini-3.1-flash-lite` |
| `gemini-3-pro-preview` | Shut down | `gemini-3.1-pro-preview` |
| `imagen-4` | Deprecated | `nano-banana-2` |

## Notes

- **Free Tier**: Available for developers with generous limits. Content submitted in the Free Tier may be used by Google to improve products. Grounding with Google Search is limited to 5,000 prompts per month across the Gemini 3 family.
- **Batch API**: Offers a 50% cost reduction compared to Standard pricing. Requests are processed within 24 hours.
- **Context Caching**: Supported on Paid Tier. Pricing ranges from $0.0125 to $0.40 per 1M tokens depending on the model. Storage is billed at $1.00 per 1M tokens per hour (Standard) or $4.50-$8.10 for Pro models.
- **Grounding**: Supports "Grounding with Google Search" and "Grounding with Google Maps". Paid Tier pricing is $14 per 1,000 search queries after the initial free monthly quota.
- **Latency Tiers**: Supports Standard, Flex (lower cost, variable latency), and Priority (highest throughput, lowest latency) tiers.
- **Thinking Tokens**: Gemini 3 series models include "thinking" tokens in the output price. These tokens represent the model's internal reasoning process before generating a final response.
- **Data Residency**: Enterprise tier offers options for data residency and advanced security compliance through the Gemini Enterprise Agent Platform.
- **Deprecation Policy**: Preview models are typically deprecated with at least 2 weeks' notice. Stable models have longer support cycles.
