---
provider: OpenAI
slug: openai
last_updated: 2026-08-03T09:55:07Z
sources:
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing), [developers.openai.com/api/docs/models](https://developers.openai.com/api/docs/models)  ·  **Updated:** `2026-08-03T09:55:07Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Flagship Models (GPT-5.6)

The GPT-5.6 series represents the frontier of OpenAI's reasoning and multimodal capabilities, featuring a unified 1.05M token context window and support for complex tool use including "Computer Use."

| Model ID | Aliases | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | `gpt-5.6` | text, image | text | 1,050,000 | 128,000 | Feb 16, 2026 | Stable |
| `gpt-5.6-terra` | — | text, image | text | 1,050,000 | 128,000 | Feb 16, 2026 | Stable |
| `gpt-5.6-luna` | — | text, image | text | 1,050,000 | 128,000 | Feb 16, 2026 | Stable |

| Model ID | Languages | Capabilities | Latency Tier / SLA | Rate Limits |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | Multilingual | function calling, structured outputs, streaming, system instructions, caching, batch, vision, web search, file search, computer use | Standard, Batch, Flex, Fast | see Notes |
| `gpt-5.6-terra` | Multilingual | function calling, structured outputs, streaming, system instructions, caching, batch, vision, web search, file search, computer use | Standard, Batch, Flex, Fast | see Notes |
| `gpt-5.6-luna` | Multilingual | function calling, structured outputs, streaming, system instructions, caching, batch, vision, web search, file search, computer use | Standard, Batch, Flex, Fast | see Notes |

#### GPT-5.6 Pricing (USD per 1M tokens)

| Model ID | Tier | Input | Cached Input | Cache Writes | Output |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | Standard (Short Context) | $5.00 | $0.50 | $6.25 | $30.00 |
| | Standard (Long Context) | $10.00 | $1.00 | $12.50 | $45.00 |
| | Batch / Flex (Short) | $2.50 | $0.25 | $3.125 | $15.00 |
| | Fast mode (Short) | $10.00 | $1.00 | $12.50 | $60.00 |
| `gpt-5.6-terra` | Standard (Short Context) | $2.00 | $0.20 | $2.50 | $12.00 |
| | Standard (Long Context) | $4.00 | $0.40 | $5.00 | $18.00 |
| | Batch / Flex (Short) | $1.00 | $0.10 | $1.25 | $6.00 |
| | Fast mode (Short) | $4.00 | $0.40 | $5.00 | $24.00 |
| `gpt-5.6-luna` | Standard (Short Context) | $0.20 | $0.02 | $0.25 | $1.20 |
| | Standard (Long Context) | $0.40 | $0.04 | $0.50 | $1.80 |
| | Batch / Flex (Short) | $0.10 | $0.01 | $0.125 | $0.60 |
| | Fast mode (Short) | $0.40 | $0.04 | $0.50 | $2.40 |

### Standard Models (GPT-5.5 & GPT-5.4)

These models provide a range of performance and cost options, including specialized "Pro" versions for high-compute tasks and "Nano" for extreme efficiency.

| Model ID | Aliases | Inputs | Outputs | Context Window | Max Output | Cutoff | Stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.5` | — | text, image | text | — | — | — | Stable |
| `gpt-5.5-pro` | — | text, image | text | — | — | — | Stable |
| `gpt-5.4` | — | text, image | text | — | — | — | Stable |
| `gpt-5.4-mini` | — | text, image | text | — | — | — | Stable |
| `gpt-5.4-nano` | — | text, image | text | — | — | — | Stable |
| `gpt-5.4-pro` | — | text, image | text | — | — | — | Stable |

| Model ID | Capabilities | Latency Tier | Pricing (Standard Input/Output per MTok) |
| :--- | :--- | :--- | :--- |
| `gpt-5.5` | function calling, structured outputs, streaming, vision, batch | Standard, Batch, Flex, Fast | $5.00 / $30.00 |
| `gpt-5.5-pro` | function calling, structured outputs, streaming, vision, batch | Standard, Batch, Flex | $30.00 / $180.00 |
| `gpt-5.4` | function calling, structured outputs, streaming, vision, batch | Standard, Batch, Flex, Fast | $2.50 / $15.00 |
| `gpt-5.4-mini` | function calling, structured outputs, streaming, vision, batch | Standard, Batch, Flex, Fast | $0.75 / $4.50 |
| `gpt-5.4-nano` | function calling, structured outputs, streaming, vision, batch | Standard, Batch, Flex | $0.20 / $1.25 |
| `gpt-5.4-pro` | function calling, structured outputs, streaming, vision, batch | Standard, Batch, Flex | $30.00 / $180.00 |

### Realtime & Audio

Models optimized for low-latency speech-to-speech, translation, and transcription.

| Model ID | Inputs | Outputs | Release Stage | Capabilities | Pricing (Input/Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2.1` | text, audio, image | text, audio | Stable | realtime, tool use, vision | Audio: $32.00 / $64.00<br>Text: $4.00 / $24.00 |
| `gpt-realtime-2.1-mini` | text, audio, image | text, audio | Stable | realtime, tool use, vision | Audio: $10.00 / $20.00<br>Text: $0.60 / $2.40 |
| `gpt-realtime-translate` | audio | audio | Stable | live translation | $0.034 / minute |
| `gpt-live-transcribe` | audio | text | Stable | live transcription | $0.017 / minute |
| `gpt-realtime-whisper` | audio | text | Stable | streaming transcription | $0.017 / minute |
| `gpt-transcribe` | audio | text | Stable | file transcription | $0.0045 / minute |
| `gpt-4o-transcribe` | audio | text | Stable | transcription | $0.006 / minute |
| `gpt-4o-mini-transcribe` | audio | text | Stable | transcription | $0.003 / minute |

### Image Generation

| Model ID | Inputs | Output Resolution | Price (Standard) | Price (Batch) |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-image-2` | text, image | — | $8.00 / MTok (Img In)<br>$30.00 / MTok (Img Out) | $4.00 / MTok (Img In)<br>$15.00 / MTok (Img Out) |
| `gpt-image-1.5` | text, image | — | $8.00 / MTok (Img In)<br>$32.00 / MTok (Img Out) | $4.00 / MTok (Img In)<br>$16.00 / MTok (Img Out) |
| `gpt-image-1-mini` | text, image | — | $2.50 / MTok (Img In)<br>$8.00 / MTok (Img Out) | $1.25 / MTok (Img In)<br>$4.00 / MTok (Img Out) |

### Video Generation (Sora)

| Model ID | Max Duration | Resolutions | Price per Second (Standard) | Price per Second (Batch) |
| :--- | :--- | :--- | :--- | :--- |
| `sora-2` | — | 720p (Portrait/Landscape) | $0.10 | $0.05 |
| `sora-2-pro` | — | 720p, 1024p, 1080p | $0.30 - $0.70 | $0.15 - $0.35 |

### Specialized & Deprecated

| Model ID | Category | Description | Pricing |
| :--- | :--- | :--- | :--- |
| `chat-latest` | ChatGPT | Latest chat-optimized model | $5.00 In / $30.00 Out |
| `gpt-5.3-codex` | Codex | Optimized for code generation | $1.75 In / $14.00 Out |
| `gpt-5.4-cyber` | Cyber | Specialized for cybersecurity | — |
| `o4-mini-2025-04-16` | Fine-tuning | Supervised fine-tuning model | $100.00 / hour (Training) |
| `gpt-realtime-mini` | Realtime | Cost-efficient voice model | Deprecated |
| `gpt-4o-mini-tts` | Speech | Text-to-speech model | Deprecated |

## Notes

- **Batch & Flex Discounts**: OpenAI offers a 50% discount on input and output tokens for requests submitted via the Batch API or the Flex processing tier.
- **Prompt Caching**: Caching is automatic. Input tokens that hit the cache are billed at a 90% discount (e.g., $0.50 vs $5.00 for `gpt-5.6-sol`). However, a "Cache Writes" fee applies when the model writes new content to the cache, typically priced slightly higher than the standard input rate.
- **Fast Mode**: Formerly known as "Priority processing," Fast mode provides the lowest latency at a 2x premium over standard rates. Requests can use `service_tier: "fast"` or the legacy `service_tier: "priority"`.
- **Data Residency**: Regional processing endpoints (e.g., EU-only) incur a 10% pricing uplift for all models released on or after March 5, 2026.
- **Rate Limit Tiers**: OpenAI uses a 5-tier system (Tier 1 to Tier 5) based on account age and total spend. Limits are typically defined in Requests Per Minute (RPM) and Tokens Per Minute (TPM). Tier 5 accounts generally have access to the highest limits and "Fast mode" processing.
- **Web Search Tool**: Billed at $10.00 per 1,000 calls. For reasoning models (GPT-5, o-series), search content tokens are billed at standard model rates. For non-reasoning models in preview, search content tokens are free or billed as a fixed block of 8,000 tokens.
- **Fine-tuning Policy**: The fine-tuning platform is currently winding down and is no longer accessible to new users. Existing users can continue training for a limited time; fine-tuned models remain available until their base models are deprecated.
- **Deprecation Policy**: OpenAI typically provides a 6-month notice before retiring a model. Deprecated models remain available for inference until their announced shutdown date.
