---
provider: Google
slug: google
last_updated: 2026-07-20T09:24:02Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-07-20T09:24:02Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Gemini 3.5 Series (Chat / Reasoning)

The Gemini 3.5 series represents the latest generation of frontier models, featuring native reasoning ("thinking") capabilities and superior speed for agentic and coding tasks.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-flash` | `gemini-3.5-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context, thinking, grounding with Google Maps | Fast | **Standard:** $1.50 (In) / $9.00 (Out)<br>**Batch/Flex:** $0.75 (In) / $4.50 (Out)<br>**Priority:** $2.70 (In) / $16.20 (Out)<br>**Cached:** $0.15 |

### Gemini 3.1 Series (Chat / Reasoning)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-customtools` | text, image, audio, video, PDF, code | text | 2,097,152 | 8,192 | — | Preview | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context, thinking, grounding with Google Maps | Moderate | **Standard (<=200k):** $2.00 (In) / $12.00 (Out)<br>**Standard (>200k):** $4.00 (In) / $18.00 (Out)<br>**Batch/Flex:** $1.00 (In) / $6.00 (Out)<br>**Priority:** $3.60 (In) / $21.60 (Out) |
| `gemini-3.1-flash-lite` | — | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context, thinking | Fastest | **Standard:** $0.25 (In) / $1.50 (Out)<br>**Batch/Flex:** $0.125 (In) / $0.75 (Out)<br>**Priority:** $0.45 (In) / $2.70 (Out) |
| `gemini-3-flash-preview` | — | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | — | Preview | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context | Fast | **Standard:** $0.50 (In) / $3.00 (Out)<br>**Batch/Flex:** $0.25 (In) / $1.50 (Out)<br>**Priority:** $0.90 (In) / $5.40 (Out) |

### Gemini 2.5 Series (Chat / Reasoning)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | `gemini-2.5-pro-latest` | text, image, audio, video, PDF, code | text | 2,097,152 | 8,192 | Jan 2025 | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context, thinking | Moderate | **Standard (<=200k):** $1.25 (In) / $10.00 (Out)<br>**Standard (>200k):** $2.50 (In) / $15.00 (Out)<br>**Batch/Flex:** $0.625 (In) / $5.00 (Out)<br>**Priority:** $2.25 (In) / $18.00 (Out) |
| `gemini-2.5-flash` | `gemini-2.5-flash-latest` | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | Jan 2025 | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context, thinking | Fast | **Standard:** $0.10 (In) / $0.40 (Out)<br>**Batch:** $0.05 (In) / $0.20 (Out) |
| `gemini-2.5-flash-lite` | — | text, image, audio, video, PDF, code | text | 1,048,576 | 8,192 | Jan 2025 | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, URL context | Fastest | **Standard:** $0.075 (In) / $0.30 (Out) |

### Realtime / Audio

Models optimized for low-latency bidirectional voice, video, and translation.

| Model ID | Aliases | Inputs | Outputs | Context Window | Release Stage | Languages | Capabilities | Latency | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | — | audio | audio | — | Preview | 70+ | live API, streaming, multilingual | Realtime | $3.50/MTok (In), $21.00/MTok (Out)<br>Approx. $0.0368/min |
| `gemini-3.1-flash-live-preview` | — | text, image, audio, video | text, audio | 1,048,576 | Preview | — | live API, streaming, multimodal awareness | Realtime | **Text:** $0.75 (In) / $4.50 (Out)<br>**Audio:** $3.00 (In) / $12.00 (Out) |
| `gemini-3.1-flash-tts-preview` | — | text | audio | — | Preview | — | audio generation, streaming | Realtime | **Text:** $1.00 (In)<br>**Audio:** $20.00 (Out) |
| `gemini-2.5-flash-live-preview` | — | text, image, audio, video | text, audio | 1,048,576 | Preview | — | live API, streaming | Realtime | — |

### Image Generation

| Model ID | Aliases | Inputs | Output Resolution | Price per Image | Price per MTok |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-flash-image` | `nano-banana-2` | text, image | 512px to 4096px | $0.045 (0.5K), $0.067 (1K), $0.101 (2K), $0.151 (4K) | $0.50 (In) / $60.00 (Out) |
| `gemini-3.1-flash-lite-image` | `nano-banana-2-lite` | text, image | 1024x1024 | $0.0336 (1K) | $0.25 (In) / $30.00 (Out) |
| `gemini-3-pro-image` | `nano-banana-pro` | text, image | 1024x1024 to 4096px | $0.134 (1K/2K), $0.24 (4K) | $2.00 (In) / $120.00 (Out) |

### Video Generation

| Model ID | Max Duration | Supported Resolutions | Price per Second | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-omni-flash-preview` | — | 720p | $0.10 | $1.50 (In) / $17.50 (Out) |
| `veo-3.1-preview` | — | — | — | — |

### Embeddings

| Model ID | Dimensions | Max Input | Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2` | — | — | text, image, video, audio, PDF | — |
| `text-embedding-004` | 768 (reducible) | 2048 | text | $0.10 |

### Specialized / Agents

| Model ID | Description | Pricing |
| :--- | :--- | :--- |
| `computer-use-preview` | Specialized model for UI automation (clicking, typing, navigating). | — |
| `gemini-deep-research-preview` | Autonomous agent for multi-step research across hundreds of sources. | — |
| `antigravity-agent-preview` | General-purpose agent running in a secure, isolated Linux sandbox. | — |
| `gemini-robotics-er-1.6-preview` | Embodied reasoning for robotic agents and physical space understanding. | — |

### Deprecated

| Model ID | Shutdown Date | Replacement |
| :--- | :--- | :--- |
| `gemini-2.0-flash` | Shut down | `gemini-2.5-flash` |
| `gemini-2.0-flash-lite` | Shut down | `gemini-2.5-flash-lite` |
| `gemini-3.1-flash-lite-preview` | Shut down | `gemini-3.1-flash-lite` |
| `gemini-3-pro-preview` | Shut down | `gemini-3.1-pro-preview` |
| `imagen-4` | Deprecated | `gemini-3.1-flash-image` |

## Notes

- **Free Tier**: Available for developers and small projects. Content submitted via the free tier is used to improve Google products. Rate limits are significantly lower (e.g., 1,500 RPD for Gemini 2.5 Pro).
- **Paid Tier**: Content is not used to improve Google products. Provides access to higher rate limits, Context Caching, and the Batch API.
- **Batch API**: Offers a 50% cost reduction on input and output tokens for non-time-sensitive tasks.
- **Context Caching**: Available on the paid tier. Storage is billed at $1.00 per 1,000,000 tokens per hour (for Gemini 3.5 series). Caching reduces input costs by up to 90% for repeated content.
- **Grounding**: Grounding with Google Search is billed at $14 per 1,000 search queries after a free monthly allowance of 5,000 prompts (shared across Gemini 3 models). Grounding with Google Maps is also $14 per 1,000 queries.
- **Thinking Tokens**: For models with reasoning capabilities (e.g., Gemini 3.5 Flash), output pricing includes the "thinking" tokens generated during the reasoning phase.
- **Rate Limit Tiers**: Google uses a 5-tier system based on monthly spend. Tier 1 (lowest paid) typically allows 2,000 RPM for Flash models and 50 RPM for Pro models.
- **Latency Tiers**: Models support Standard, Flex (lower cost, higher latency), and Priority (guaranteed throughput, higher cost) tiers.
