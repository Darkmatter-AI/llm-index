---
provider: OpenAI
slug: openai
last_updated: 2026-05-19T11:27:53Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [openai.com/api/pricing](https://openai.com/api/pricing/), [platform.openai.com/docs/models](https://platform.openai.com/docs/models)  ·  **Updated:** `2026-05-19T11:27:53Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models
These models represent the current state-of-the-art for general-purpose reasoning, coding, and professional workflows. All models in this category support text and image inputs.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.5` | `gpt-5.5-latest` | text, image | text | 1,000,000 | 128,000 | Dec 2025 | Stable | Multilingual |
| `gpt-5.4` | `gpt-5.4-latest` | text, image | text | 1,000,000 | 128,000 | Aug 2025 | Stable | Multilingual |
| `gpt-5.4-mini` | `gpt-5.4-mini-latest` | text, image | text | 400,000 | 128,000 | Aug 2025 | Stable | Multilingual |
| `gpt-5.4-nano` | — | text, image | text | — | — | Aug 2025 | Stable | Multilingual |
| `gpt-5.1` | — | text, image | text | — | — | — | Stable | Multilingual |
| `gpt-5.2` | — | text, image | text | — | — | — | Stable | Multilingual |

| Model ID | Capabilities | Latency Tier / SLA | Pricing (Input/Cached/Output per MTok) |
| :--- | :--- | :--- | :--- |
| `gpt-5.5` | function calling, web search, file search, computer use, structured outputs, streaming, system instructions, prompt caching, batch | Standard, Priority, Batch | $5.00 / $0.50 / $30.00 |
| `gpt-5.4` | function calling, web search, file search, computer use, structured outputs, streaming, system instructions, prompt caching, batch | Standard, Priority, Batch | $2.50 / $0.25 / $15.00 |
| `gpt-5.4-mini` | function calling, web search, file search, computer use, structured outputs, streaming, system instructions, prompt caching, batch | Faster, Batch | $0.75 / $0.075 / $4.50 |
| `gpt-5.4-nano` | function calling, structured outputs, streaming, prompt caching | Fastest | — |
| `gpt-5.1` | function calling, structured outputs, streaming | Standard | — |
| `gpt-5.2` | function calling, structured outputs, streaming | Standard | — |

### Reasoning Models
Optimized for complex, multi-step problems in STEM and coding. These models "think" before responding.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `o3` | — | text, image | text | — | — | — | Stable | reasoning, function calling, structured outputs |
| `o3-deep-research` | — | text, image | text | — | — | — | Stable | reasoning, web search, file search |
| `o3-pro-2025-06-10` | — | text, image | text | — | — | Jun 2025 | Stable | reasoning, priority inference |
| `o4-mini` | — | text, image | text | — | — | — | Stable | reasoning, function calling |
| `o4-mini-deep-research` | — | text, image | text | — | — | — | Stable | reasoning, web search |
| `o1` | `o1-2024-12-17` | text, image | text | 128,000 | 100,000 | Oct 2023 | Stable | reasoning, function calling, structured outputs |
| `o1-pro` | — | text, image | text | 128,000 | 100,000 | Oct 2023 | Stable | reasoning, priority inference |

### Multimodal & Realtime
Models designed for low-latency voice, audio, and image interactions.

| Model ID | Inputs | Outputs | Latency Tier | Pricing (Input/Cached/Output per MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2` | text, audio, image | text, audio | Realtime | Audio: $32.00 / $0.40 / $64.00<br>Text: $4.00 / $0.40 / $24.00<br>Image: $5.00 / $0.50 / — |
| `gpt-realtime-1.5` | text, audio | text, audio | Realtime | — |
| `gpt-realtime-mini` | text, audio | text, audio | Realtime | — |
| `gpt-image-2` | text, image | image, text | Standard | Image: $8.00 / $2.00 / $30.00<br>Text: $5.00 / $1.25 / — |

| Model ID | Function | Pricing |
| :--- | :--- | :--- |
| `gpt-realtime-translate` | Live speech-to-speech translation | $0.034 per minute |
| `gpt-realtime-whisper` | Streaming speech-to-text | $0.017 per minute |

### Legacy & Previews
Older flagship models and experimental previews.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-4o` | `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable |
| `gpt-4o-mini` | `gpt-4o-mini-2024-07-18` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable |
| `gpt-4.5-preview` | — | text, image | text | — | — | — | Preview |
| `computer-use-preview` | — | text, image | text | — | — | — | Preview |
| `codex-mini-latest` | — | text, code | text, code | — | — | — | Stable |

### Specialized Models

**Embeddings**
| Model ID | Output Dimensions | Max Input | Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `text-embedding-3-small` | 1536 (Matryoshka) | 8,191 | text | $0.02 |
| `text-embedding-3-large` | 3072 (Matryoshka) | 8,191 | text | $0.13 |
| `text-embedding-ada-002` | 1536 | 8,191 | text | $0.10 |

**Audio (Non-Realtime)**
| Model ID | Direction | Supported Languages | Price |
| :--- | :--- | :--- | :--- |
| `whisper-1` | STT / Translation | 98+ | $0.006 / minute |
| `tts-1` | TTS | — | $15.00 / M characters |
| `tts-1-hd` | TTS | — | $30.00 / M characters |
| `gpt-4o-mini-tts` | TTS | — | — |
| `gpt-4o-transcribe` | STT | — | — |

**Moderation**
| Model ID | Function | Pricing |
| :--- | :--- | :--- |
| `omni-moderation-latest` | Multimodal content safety | Free for OpenAI API traffic |
| `text-moderation-latest` | Text content safety | Free for OpenAI API traffic |

## Notes

*   **Batch API:** Offers a 50% discount on input and output tokens for all supported models. Requests are processed asynchronously with a guaranteed 24-hour turnaround.
*   **Prompt Caching:** Automatic for GPT-5, GPT-4o, and o-series models. Cached tokens receive a discount (e.g., 90% for GPT-5.5, 50% for GPT-4o). TTL is typically 5–10 minutes of inactivity.
*   **Data Residency:** Regional processing and data residency options are available for an additional 10% surcharge on standard rates.
*   **Service Tiers:** 
    *   **Standard:** Default pay-as-you-go.
    *   **Priority:** Reliable high-speed performance for production workloads.
    *   **Flex:** Lower cost for non-production tasks; subject to resource availability and higher latency.
    *   **Scale:** Reserved capacity for enterprise customers.
*   **Rate Limits:** Based on usage tiers (Tier 1 to Tier 5). Tier 5 typically allows up to 10,000 RPM and 10M TPM on flagship models.
*   **Tool Pricing:** Web search is billed at $10.00 per 1,000 calls. Search content tokens are free.
*   **Containers:** Secure code execution environments are billed at $0.03 per GB per 20-minute session (starting March 31, 2026).
*   **Context Tiering:** Standard pricing for GPT-5 models applies to context lengths under 270K tokens; higher context usage may incur different rates.
