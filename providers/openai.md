---
provider: OpenAI
slug: openai
last_updated: 2026-06-22T08:17:54Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [openai.com/api/pricing](https://openai.com/api/pricing/), [platform.openai.com/docs/models](https://platform.openai.com/docs/models)  ·  **Updated:** `2026-06-22T08:17:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models
Our most advanced models for complex reasoning, coding, and professional workflows. These models support tiered pricing based on context length.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.5` | `gpt-5.5-latest`, `gpt-5.5-2026-05-15` | text, image | text | 1,000,000 | 128,000 | Dec 2025 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, file search, web search, computer use, vision, multilingual |
| `gpt-5.4` | `gpt-5.4-latest`, `gpt-5.4-2026-03-10` | text, image | text | 1,000,000 | 128,000 | Aug 2025 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, file search, web search, computer use, vision, multilingual |
| `gpt-5.4-mini` | `gpt-5.4-mini-latest`, `gpt-5.4-mini-2026-03-10` | text, image | text | 400,000 | 128,000 | Aug 2025 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, file search, web search, computer use, vision, multilingual |
| `gpt-5.4-nano` | — | text, image | text | — | — | Aug 2025 | Preview | vision, multilingual, prompt caching, batch |

#### Frontier Pricing (Standard)
*Rates for context lengths under 270,000 tokens.*

| Model ID | Input $/MTok | Cached Input $/MTok | Output $/MTok | Latency Tier |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-5.5` | $5.00 | $0.50 | $30.00 | Fast |
| `gpt-5.4` | $2.50 | $0.25 | $15.00 | Fast |
| `gpt-5.4-mini` | $0.75 | $0.075 | $4.50 | Faster |

### Reasoning Models
Models designed to spend more time thinking before producing a response, ideal for complex, multi-step problems and STEM use cases.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `o3` | `o3-latest`, `o3-2025-01-31` | text, image | text | 200,000 | 100,000 | — | Stable | reasoning, thinking, function calling, structured outputs, vision, prompt caching, batch |
| `o3-deep-research` | — | text, image | text | — | — | — | Preview | reasoning, thinking, web search, file search, vision |
| `o3-pro-2025-06-10` | — | text, image | text | — | — | — | Stable | reasoning, thinking, extended thinking, vision |
| `o4-mini` | `o4-mini-latest` | text, image | text | 128,000 | 65,536 | — | Stable | reasoning, thinking, function calling, structured outputs, vision, prompt caching, batch |
| `o4-mini-deep-research` | — | text, image | text | — | — | — | Preview | reasoning, thinking, web search, vision |
| `o1` | `o1-latest`, `o1-2024-12-17` | text, image | text | 200,000 | 100,000 | Oct 2023 | Stable | reasoning, thinking, function calling, structured outputs, vision, prompt caching, batch |
| `o1-pro` | — | text, image | text | — | — | Oct 2023 | Stable | reasoning, thinking, extended thinking, vision |

### Chat Models
General-purpose models optimized for conversational interaction and low latency.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-4.1` | `gpt-4.1-latest` | text, image | text | 128,000 | 16,384 | — | Stable | function calling, structured outputs, vision, prompt caching, batch |
| `gpt-4.1-mini` | `gpt-4.1-mini-latest` | text, image | text | 128,000 | 16,384 | — | Stable | function calling, structured outputs, vision, prompt caching, batch |
| `gpt-4.1-nano` | — | text, image | text | — | — | — | Preview | vision, prompt caching, batch |
| `gpt-4.5-preview` | — | text, image | text | 128,000 | 16,384 | — | Preview | function calling, structured outputs, vision, prompt caching |
| `gpt-4o` | `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable | function calling, structured outputs, vision, prompt caching, batch, fine-tuning |
| `gpt-4o-mini` | `gpt-4o-mini-2024-07-18` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable | function calling, structured outputs, vision, prompt caching, batch, fine-tuning |

### Realtime & Audio
Models built for low-latency voice interactions, live translation, and transcription.

| Model ID | Inputs | Outputs | Release Stage | Capabilities | Pricing (Input / Cached / Output) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2` | text, audio | text, audio | Preview | voice, translation, transcription | Audio: $32.00 / $0.40 / $64.00 per MTok<br>Text: $4.00 / $0.40 / $24.00 per MTok<br>Image: $5.00 / $0.50 / — per MTok |
| `gpt-realtime-1.5` | text, audio | text, audio | Stable | voice, translation, transcription | — |
| `gpt-realtime-mini` | text, audio | text, audio | Stable | voice, translation, transcription | — |
| `gpt-realtime-translate` | audio | audio | Stable | live translation | $0.034 per minute ($0.00057 per second) |
| `gpt-realtime-whisper` | audio | text | Stable | live transcription | $0.017 per minute ($0.00028 per second) |
| `gpt-4o-transcribe` | audio | text | Stable | speech-to-text | — |
| `gpt-4o-mini-transcribe` | audio | text | Stable | speech-to-text | — |
| `whisper-1` | audio | text | Stable | transcription, translation | $0.006 / minute |

### Image Generation
State-of-the-art models for generating and editing images.

| Model ID | Inputs | Output Resolution | Price per Image (Standard) | Price per 1M Tokens |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-image-2` | text, image | — | — | Input: $8.00<br>Cached: $2.00<br>Output: $30.00 |
| `dall-e-3` | text | 1024×1024, 1024×1792, 1792×1024 | $0.040 (Standard)<br>$0.080 (HD) | — |
| `dall-e-2` | text, image+mask | 256×256, 512×512, 1024×1024 | $0.016 (256)<br>$0.018 (512)<br>$0.020 (1024) | — |

### Embeddings
Models for converting text into numerical vectors for search and retrieval.

| Model ID | Max Input | Output Dimensions | Price per MTok |
| :--- | :--- | :--- | :--- |
| `text-embedding-3-small` | 8,191 | 512, 1536 (Matryoshka) | $0.02 |
| `text-embedding-3-large` | 8,191 | 256, 1024, 3072 (Matryoshka) | $0.13 |
| `text-embedding-ada-002` | 8,191 | 1536 | $0.10 |

### Specialized & Tools
Built-in tools and specialized models for safety and infrastructure.

| Model ID | Function | Pricing |
| :--- | :--- | :--- |
| `omni-moderation-latest` | Multimodal safety filtering | Free |
| `text-moderation-latest` | Text safety filtering | Free |
| `web-search` | Grounding with live web data | $10.00 / 1,000 calls (Content tokens free) |
| `containers` | Secure code execution environments | $0.03 / GB per session (Starting March 31, 2026) |

### Deprecated
Models scheduled for retirement or no longer recommended for new projects.

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `gpt-4o-mini-tts` | — | `gpt-realtime-2` |
| `gpt-3.5-turbo-0125` | — | `gpt-4o-mini` |
| `gpt-4-0613` | — | `gpt-4o` |

## Notes

- **Batch API**: Offers a 50% discount on input and output tokens for asynchronous tasks processed within 24 hours.
- **Prompt Caching**: Automatically applied to supported models (GPT-5.5, 5.4, 5.4-mini, o3, o4-mini, o1, GPT-4o, GPT-4o-mini). Cached input tokens are billed at a ~90% discount for Frontier models and 50% for others.
- **Data Residency**: Regional processing and data residency options are available for an additional 10% premium on token pricing.
- **Rate Limit Tiers**: OpenAI uses a 5-tier system (Tier 1 to Tier 5) based on account age and total spend. Limits are defined per model in RPM (Requests Per Minute), TPM (Tokens Per Minute), and RPD (Requests Per Day).
- **Context Tiering**: Frontier models (GPT-5.5, 5.4) use standard pricing for context lengths under 270,000 tokens; higher context usage may incur different rates.
- **Service Tiers**: Supports `Standard`, `Priority` (high-speed, pay-as-you-go), `Flex` (lower cost, slower/variable availability), and `Scale` (dedicated capacity for enterprise).
- **Fine-tuning**: Available for `gpt-4o`, `gpt-4o-mini`, and `gpt-3.5-turbo`. Training is billed per MTok, and inference is billed at a premium over base model rates.
- **Usage Tracking**: Billed separately from ChatGPT subscriptions. Usage is tracked in the API Dashboard with monthly budget limits and notification thresholds.
