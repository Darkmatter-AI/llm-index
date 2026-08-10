---
provider: OpenAI
slug: openai
last_updated: 2026-08-10T07:49:39Z
sources:
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing), [developers.openai.com/api/docs/models](https://developers.openai.com/api/docs/models)  ·  **Updated:** `2026-08-10T07:49:39Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models

Flagship models designed for complex reasoning, coding, and professional workflows. All models in this category support text and image inputs with text output.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | `gpt-5.6` | text, image | text | 1,050,000 | 131,072 | Feb 2026 | Stable | Multilingual | function calling, web search, file search, computer use, vision, multilingual, prompt caching, batch, flex inference, fast mode | Standard, Fast, Batch, Flex | see Notes | Standard (Short): $5.00 input / $0.50 cached / $30.00 output<br>Standard (Long): $10.00 input / $1.00 cached / $45.00 output |
| `gpt-5.6-terra` | — | text, image | text | 1,050,000 | 131,072 | Feb 2026 | Stable | Multilingual | function calling, web search, file search, computer use, vision, multilingual, prompt caching, batch, flex inference, fast mode | Standard, Fast, Batch, Flex | see Notes | Standard (Short): $2.00 input / $0.20 cached / $12.00 output<br>Standard (Long): $4.00 input / $0.40 cached / $18.00 output |
| `gpt-5.6-luna` | — | text, image | text | 1,050,000 | 131,072 | Feb 2026 | Stable | Multilingual | function calling, web search, file search, computer use, vision, multilingual, prompt caching, batch, flex inference, fast mode | Standard, Fast, Batch, Flex | see Notes | Standard (Short): $0.20 input / $0.02 cached / $1.20 output<br>Standard (Long): $0.40 input / $0.04 cached / $1.80 output |

### Previous Generation

Models from the GPT-5.5 and GPT-5.4 series, offering a range of performance and cost profiles.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.5` | — | text, image | text | 1,050,000 | 131,072 | — | Stable | Multilingual | function calling, vision, prompt caching, batch, flex inference, fast mode | Standard, Fast, Batch, Flex | see Notes | Standard (Short): $5.00 input / $0.50 cached / $30.00 output<br>Standard (Long): $10.00 input / $1.00 cached / $45.00 output |
| `gpt-5.5-pro` | — | text, image | text | 1,050,000 | 131,072 | — | Stable | Multilingual | function calling, vision, batch, flex inference | Standard, Batch, Flex | see Notes | Standard (Short): $30.00 input / $180.00 output<br>Standard (Long): $60.00 input / $270.00 output |
| `gpt-5.4` | — | text, image | text | 1,050,000 | 131,072 | — | Stable | Multilingual | function calling, vision, prompt caching, batch, flex inference, fast mode | Standard, Fast, Batch, Flex | see Notes | Standard (Short): $2.50 input / $0.25 cached / $15.00 output<br>Standard (Long): $5.00 input / $0.50 cached / $22.50 output |
| `gpt-5.4-mini` | — | text, image | text | 1,050,000 | 131,072 | — | Stable | Multilingual | function calling, vision, prompt caching, batch, flex inference, fast mode | Standard, Fast, Batch, Flex | see Notes | Standard (Short): $0.75 input / $0.075 cached / $4.50 output |
| `gpt-5.4-nano` | — | text, image | text | 1,050,000 | 131,072 | — | Stable | Multilingual | function calling, vision, prompt caching, batch, flex inference | Standard, Batch, Flex | see Notes | Standard (Short): $0.20 input / $0.02 cached / $1.25 output |
| `gpt-5.4-pro` | — | text, image | text | 1,050,000 | 131,072 | — | Stable | Multilingual | function calling, vision, batch, flex inference | Standard, Batch, Flex | see Notes | Standard (Short): $30.00 input / $180.00 output<br>Standard (Long): $60.00 input / $270.00 output |

### Realtime & Audio

Models optimized for low-latency speech-to-speech, transcription, and translation.

| Model ID | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Capabilities | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2.1` | text, audio, image | text, audio | — | — | — | Stable | realtime, tool use, vision | Audio: $32.00 input / $0.40 cached / $64.00 output<br>Text: $4.00 input / $0.40 cached / $24.00 output<br>Image: $5.00 input / $0.50 cached |
| `gpt-realtime-2.1-mini` | text, audio, image | text, audio | — | — | — | Stable | realtime, tool use, vision | Audio: $10.00 input / $0.30 cached / $20.00 output<br>Text: $0.60 input / $0.06 cached / $2.40 output<br>Image: $0.80 input / $0.08 cached |
| `gpt-realtime-2` | text, audio | text, audio | — | — | — | Stable | realtime, tool use | see `gpt-realtime-2.1` |
| `gpt-realtime-translate` | audio | audio | — | — | — | Stable | streaming translation | $0.034 / minute |
| `gpt-realtime-1.5` | audio | audio | — | — | — | Stable | voice-to-voice | — |

#### Transcription & Speech

| Model ID | Direction | Supported Languages | Price |
| :--- | :--- | :--- | :--- |
| `gpt-transcribe` | audio to text | — | $0.0045 / minute |
| `gpt-live-transcribe` | audio to text | — | $0.017 / minute |
| `gpt-realtime-whisper` | audio to text | — | $0.017 / minute |
| `gpt-4o-transcribe` | audio to text | — | $2.50 input MTok / $10.00 output MTok ($0.006 / minute) |
| `gpt-4o-mini-transcribe` | audio to text | — | $1.25 input MTok / $5.00 output MTok ($0.003 / minute) |
| `gpt-4o-mini-tts` | text to audio | — | — |

### Image & Video

#### Image Generation

| Model ID | Inputs | Output Resolution(s) | Price (Standard) | Price (Batch) |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-image-2` | text, image | — | Image: $8.00 / MTok input, $30.00 / MTok output<br>Text: $5.00 / MTok input | Image: $4.00 / MTok input, $15.00 / MTok output<br>Text: $2.50 / MTok input |
| `gpt-image-1.5` | text, image | — | Image: $8.00 / MTok input, $32.00 / MTok output<br>Text: $5.00 / MTok input, $10.00 / MTok output | Image: $4.00 / MTok input, $16.00 / MTok output<br>Text: $2.50 / MTok input, $5.00 / MTok output |
| `gpt-image-1-mini` | text, image | — | Image: $2.50 / MTok input, $8.00 / MTok output<br>Text: $2.00 / MTok input | Image: $1.25 / MTok input, $4.00 / MTok output<br>Text: $1.00 / MTok input |

#### Video Generation

| Model ID | Max Duration | Supported Resolutions | Price per second (Standard) | Price per second (Batch) |
| :--- | :--- | :--- | :--- | :--- |
| `sora-2` | — | 720p (720x1280, 1280x720) | $0.10 | $0.05 |
| `sora-2-pro` | — | 720p, 1024p, 1080p | $0.30 (720p), $0.50 (1024p), $0.70 (1080p) | $0.15 (720p), $0.25 (1024p), $0.35 (1080p) |

### Specialized

| Model ID | What it does | Pricing |
| :--- | :--- | :--- |
| `chat-latest` | Flagship ChatGPT model for API | $5.00 input / $0.50 cached / $30.00 output (per MTok) |
| `gpt-5.3-codex` | Optimized for code generation | $1.75 input / $0.175 cached / $14.00 output (per MTok) |
| `gpt-5.4-cyber` | Cybersecurity specialized model | — |

### Deprecated

| Model ID | Retirement Date | Notes |
| :--- | :--- | :--- |
| `gpt-realtime-mini` | — | Cost-efficient version of GPT-Realtime. |
| Fine-tuning Platform | — | Winding down; no longer accessible to new users. |

## Notes

*   **Batch & Flex Discounts**: Both Batch and Flex processing modes offer a 50% discount on standard input and output token rates.
*   **Prompt Caching**: Cached input tokens are billed at a 90% discount (e.g., $0.50 vs $5.00 for `gpt-5.6-sol`). Cache writes are billed at 1.25x the standard input rate.
*   **Fast Mode**: Formerly known as "Priority" processing (renamed July 30, 2026). Requests using `service_tier: "fast"` or `service_tier: "priority"` are billed at 2x the standard rate.
*   **Regional Processing**: Data residency endpoints incur a 10% price uplift for models released on or after March 5, 2026.
*   **Context Tiers**: Pricing for flagship models is split into "Short context" and "Long context" (typically >128K tokens), with long context input billed at 2x the short context rate.
*   **Tool Pricing**: Web search is billed at $10.00 per 1,000 calls (plus content tokens). File search storage is $0.10/GB per day (first 1GB free).
*   **Rate Limits**: OpenAI uses a Tiered system (Tier 1 to Tier 5). Limits are per-model and per-tier. For example, Tier 5 typically allows up to 10,000 RPM and 10M TPM on flagship models, while Tier 1 is significantly lower (e.g., 500 RPM / 200K TPM).
*   **Fine-tuning**: Supervised and Reinforcement fine-tuning are being phased out. Existing users can still run jobs for `o4-mini-2025-04-16` at $100.00/hour training cost.
