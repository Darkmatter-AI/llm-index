---
provider: Google
slug: google
last_updated: 2026-07-06T07:45:11Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · **Google** · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Google (Gemini)

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)  ·  **Updated:** `2026-07-06T07:45:11Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat / Multimodal

Gemini models are multimodal, supporting text, image, video, audio, PDF, and code inputs. They are grouped into generations (3.5, 3.1, 3, 2.5) and sizes (Pro, Flash, Flash-Lite).

#### Gemini 3.5

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-flash` | `gemini-3.5-flash-latest`, `gemini-3.5-flash-001` | text, image, video, audio, PDF, code | text, thinking | 1,048,576 | 8,192 | Jan 2026 | Stable | 100+ |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Cached / Output) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-flash` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard**: $1.50 / $0.15 / $9.00<br>**Batch**: $0.75 / $0.075 / $4.50<br>**Flex**: $0.75 / $0.08 / $4.50<br>**Priority**: $2.70 / $0.27 / $16.20 |

#### Gemini 3.1

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-pro-preview` | `gemini-3.1-pro-preview-customtools` | text, image, video, audio, PDF, code | text, thinking | 2,097,152 | 8,192 | Oct 2025 | Preview | 100+ |
| `gemini-3.1-flash-lite` | `gemini-3.1-flash-lite-latest` | text, image, video, audio, PDF, code | text, thinking | 1,048,576 | 8,192 | Oct 2025 | Stable | 100+ |
| `gemini-3-flash-preview` | `gemini-3-flash-preview-latest` | text, image, video, audio, PDF, code | text, thinking | 1,048,576 | 8,192 | May 2025 | Preview | 100+ |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Cached / Output) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-pro-preview` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard (<=200k)**: $2.00 / $0.20 / $12.00<br>**Standard (>200k)**: $4.00 / $0.40 / $18.00<br>**Batch (<=200k)**: $1.00 / $0.20 / $6.00<br>**Batch (>200k)**: $2.00 / $0.40 / $9.00 |
| `gemini-3.1-flash-lite` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard**: $0.25 / $0.025 / $1.50<br>**Batch**: $0.125 / $0.0125 / $0.75<br>**Priority**: $0.45 / $0.045 / $2.70 |
| `gemini-3-flash-preview` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard**: $0.50 / $0.05 / $3.00<br>**Batch**: $0.25 / $0.05 / $1.50<br>**Priority**: $0.90 / $0.09 / $5.40 |

#### Gemini 2.5

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | `gemini-2.5-pro-latest` | text, image, video, audio, PDF, code | text, thinking | 2,097,152 | 8,192 | Jan 2025 | Stable | 100+ |
| `gemini-2.5-flash` | `gemini-2.5-flash-latest` | text, image, video, audio, PDF, code | text, thinking | 1,048,576 | 8,192 | Jan 2025 | Stable | 100+ |
| `gemini-2.5-flash-lite` | `gemini-2.5-flash-lite-latest` | text, image, video, audio, PDF, code | text, thinking | 1,048,576 | 8,192 | Jan 2025 | Stable | 100+ |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Cached / Output) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-2.5-pro` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard (<=200k)**: $1.25 / $0.125 / $10.00<br>**Standard (>200k)**: $2.50 / $0.25 / $15.00<br>**Batch (<=200k)**: $0.625 / $0.125 / $5.00<br>**Batch (>200k)**: $1.25 / $0.25 / $7.50 |
| `gemini-2.5-flash` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard**: $0.30 / $0.03 / $1.20<br>**Batch**: $0.15 / $0.03 / $0.60<br>**Priority**: $0.54 / $0.054 / $2.16 |
| `gemini-2.5-flash-lite` | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, search grounding, grounding with Google Maps, URL context, thinking, priority inference, flex inference | Standard, Batch, Flex, Priority | see Notes | **Standard**: $0.10 / $0.01 / $0.40<br>**Batch**: $0.05 / $0.01 / $0.20<br>**Priority**: $0.18 / $0.018 / $0.72 |

### Realtime / Audio

Models optimized for low-latency bidirectional voice and video interactions.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Release stage | Languages | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | — | audio | audio | — | — | Preview | 70+ | live API, multilingual |
| `gemini-3.1-flash-live-preview` | — | audio, video, image, text | audio, text | — | — | Preview | — | live API, multimodal awareness |
| `gemini-2.5-flash-live-preview` | — | audio, video, image, text | audio, text | — | — | Preview | — | live API, native audio reasoning |

| Model ID | Latency tier | Pricing (Input / Output) |
| :--- | :--- | :--- |
| `gemini-3.5-live-translate-preview` | Standard | $3.50 / $21.00 per MTok (Audio: ~$0.0368/min) |
| `gemini-3.1-flash-live-preview` | Standard | **Text**: $0.75 / $4.50 per MTok<br>**Audio**: $3.00 / $12.00 per MTok<br>**Image/Video**: $1.00 / — per MTok |
| `gemini-2.5-flash-live-preview` | Standard | **Text**: $0.30 / $1.20 per MTok<br>**Audio**: $1.00 / $4.00 per MTok |

### Image Generation

| Model ID | Inputs | Output resolution(s) | Price per 1M tokens (Output) | Price per image (approx.) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-3.1-flash-image` | text, image | 512px to 4096px | $60.00 | $0.067 (1K), $0.151 (4K) |
| `gemini-3.1-flash-lite-image` | text, image, video | 1024px | $30.00 | $0.0336 (1K) |
| `gemini-3-pro-image` | text, image | 1024px to 4096px | $120.00 | $0.134 (1K/2K), $0.24 (4K) |
| `gemini-2.5-flash-image` | text, image | 1024px | $30.00 | $0.0336 (1K) |

### Video Generation

| Model ID | Max duration | Supported resolutions | Price per 1M tokens (Output) | Price per second (approx.) |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-omni-flash-preview` | — | 720p | $17.50 | $0.10 |
| `veo-3.1-preview` | — | 1080p, 4K | — | — |
| `veo-3.1-lite-preview` | — | 720p | — | — |

### Embeddings

| Model ID | Output dimensions | Max input tokens | Inputs | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-embedding-2` | 768 (Matryoshka) | 2,048 | text, image, video, audio, PDF | $0.10 |
| `gemini-embedding` | 768 | 2,048 | text | $0.10 |

### Specialized / Agents

| Model ID | Function | Pricing |
| :--- | :--- | :--- |
| `gemini-robotics-er-1.6-preview` | Embodied reasoning for robotics | Input: $1.50/MTok, Output: $9.00/MTok |
| `gemini-2.5-computer-use-preview` | UI automation and screen interaction | Input: $1.50/MTok, Output: $9.00/MTok |
| `gemini-deep-research-preview` | Autonomous multi-step research agent | $14 / 1,000 search queries + token costs |
| `antigravity-agent-preview` | Managed agent in isolated Linux sandbox | $0.05 per agent minute + token costs |

### Deprecated

| Model ID | Status | Shutdown Date |
| :--- | :--- | :--- |
| `gemini-2.0-flash` | Shut down | 2026-06-30 |
| `gemini-2.0-flash-lite` | Shut down | 2026-06-30 |
| `gemini-3.1-flash-lite-preview` | Shut down | 2026-06-30 |
| `gemini-3-pro-preview` | Shut down | 2026-06-30 |
| `imagen-4` | Deprecated | — |

## Notes

- **Free Tier**: Google offers a generous free tier for developers. Content submitted via the free tier is used to improve Google products. Rate limits are significantly lower (e.g., 2-15 RPM depending on the model).
- **Batch Discount**: The Batch API offers a 50% cost reduction compared to standard pricing. Requests are processed within 24 hours.
- **Prompt Caching**: Context caching is available for stable models. Pricing includes a one-time cache fee ($0.01 - $0.40 per MTok) and a recurring storage fee ($0.50 - $8.10 per 1M tokens per hour).
- **Grounding**: Grounding with Google Search and Google Maps is priced at $14 per 1,000 search queries. Gemini 3 models include 5,000 free prompts per month shared across the family.
- **Rate Limit Tiers**: Paid tier rate limits are divided into Tiers 1–5 based on usage and billing history. Tier 1 typically starts at 2,000 RPM for Flash and 50 RPM for Pro models.
- **Thinking Tokens**: Models with "thinking" capabilities (e.g., Gemini 3.5 Flash) include thinking tokens in the standard output price.
- **Data Residency**: Options for data residency and enterprise-grade security are available via the Gemini Enterprise Agent Platform and Vertex AI on Google Cloud.
- **Deprecation Policy**: Preview models are typically deprecated with at least 2 weeks' notice. Stable models have longer support cycles.
