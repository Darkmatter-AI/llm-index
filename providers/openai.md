---
provider: OpenAI
slug: openai
last_updated: 2026-07-31T01:00:54Z
sources:
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing), [developers.openai.com/api/docs/models](https://developers.openai.com/api/docs/models)  ·  **Updated:** `2026-07-31T01:00:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Reasoning

These models are designed for complex, multi-step problems and STEM use cases, utilizing advanced reasoning to think before responding.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | `gpt-5.6` | text, image | text | 1,050,000 | 128,000 | Feb 2026 | Stable | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, file search, web search, computer use, vision, multilingual | Standard, Priority, Batch, Scale | Input: $5.00<br>Cached: $0.50<br>Output: $30.00 |
| `gpt-5.6-terra` | — | text, image | text | 1,050,000 | 128,000 | Feb 2026 | Stable | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, file search, web search, computer use, vision, multilingual | Standard, Fast mode, Batch, Scale | Input: $2.00<br>Cached: $0.20<br>Output: $12.00 |
| `gpt-5.6-luna` | — | text, image | text | 1,050,000 | 128,000 | Feb 2026 | Stable | — | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, file search, web search, computer use, vision, multilingual | Standard, Fast mode, Batch, Scale | Input: $0.20<br>Cached: $0.02<br>Output: $1.20 |
| `o4-mini` | — | text, image | text | — | — | — | Preview | — | reasoning, vision, function calling, structured outputs | Standard, Batch | — |
| `o4-mini-deep-research` | — | text, image | text | — | — | — | Preview | — | reasoning, deep research, vision | Standard | — |
| `o3` | — | text, image | text | — | — | — | Stable | — | reasoning, vision, function calling, structured outputs | Standard, Priority, Batch | — |
| `o3-deep-research` | — | text, image | text | — | — | — | Stable | — | reasoning, deep research, vision | Standard | — |
| `o3-pro-2025-06-10` | — | text, image | text | — | — | — | Stable | — | reasoning, vision, function calling | Standard | — |
| `o1` | — | text, image | text | — | — | — | Stable | — | reasoning, vision, function calling, structured outputs | Standard, Priority, Batch | — |
| `o1-pro` | — | text, image | text | — | — | — | Stable | — | reasoning, vision, function calling | Standard | — |

### Chat

General-purpose models optimized for conversation and high-volume tasks.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.2` | — | text, image | text | — | — | — | Stable | — | function calling, structured outputs, vision | Standard, Batch | — |
| `gpt-5.1` | — | text, image | text | — | — | — | Stable | — | function calling, structured outputs, vision | Standard, Batch | — |
| `gpt-5` | — | text, image | text | — | — | — | Stable | — | function calling, structured outputs, vision | Standard, Batch | — |
| `gpt-5-mini` | — | text, image | text | — | — | — | Stable | — | function calling, structured outputs, vision | Standard, Batch | — |
| `gpt-5-nano` | — | text, image | text | — | — | — | Stable | — | function calling, structured outputs, vision | Standard, Batch | — |
| `gpt-4.5-preview` | — | text, image | text | — | — | — | Preview | — | function calling, structured outputs, vision | Standard | — |
| `gpt-4o` | `gpt-4o-2024-05-13`, `gpt-4o-2024-08-06`, `gpt-4o-2024-11-20` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable | — | function calling, structured outputs, vision, streaming | Standard, Priority, Batch | — |
| `gpt-4o-mini` | `gpt-4o-mini-2024-07-18` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable | — | function calling, structured outputs, vision, streaming | Standard, Priority, Batch | — |

### Realtime

Models designed for low-latency, streaming interactions across multiple modalities.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2.1` | — | text, audio, image | text, audio | — | — | — | Stable | — | realtime voice, reasoning, tool use, vision | Standard, Priority | Audio Input: $32.00<br>Audio Output: $64.00<br>Text Input: $4.00<br>Text Output: $24.00<br>Image Input: $5.00 |
| `gpt-realtime-2.1-mini` | — | text, audio, image | text, audio | — | — | — | Stable | — | realtime voice, reasoning, tool use, vision | Standard, Priority | Audio Input: $10.00<br>Audio Output: $20.00<br>Text Input: $0.60<br>Text Output: $2.40<br>Image Input: $0.80 |
| `gpt-realtime-2` | — | text, audio | text, audio | — | — | — | Stable | — | realtime voice, reasoning, tool use | Standard | — |
| `gpt-realtime-1.5` | — | text, audio | text, audio | — | — | — | Stable | — | realtime voice | Standard | — |

### Image

| Model ID | Inputs | Output Resolution(s) | Price per 1M Tokens | Batch Discount |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-image-2` | text, image | — | Input: $8.00<br>Cached: $2.00<br>Output: $30.00 | 50% |
| `dall-e-3` | text | 1024x1024, 1024x1792, 1792x1024 | — | — |

### Speech & Audio

| Model ID | Direction | Supported Languages | Price |
| :--- | :--- | :--- | :--- |
| `gpt-realtime-translate` | Speech-to-Speech | — | $0.034 per minute |
| `gpt-realtime-whisper` | Speech-to-Text | — | $0.017 per minute |
| `gpt-4o-transcribe` | Speech-to-Text | — | — |
| `gpt-4o-mini-transcribe` | Speech-to-Text | — | — |

### Specialized

| Model ID | Description | Pricing |
| :--- | :--- | :--- |
| `computer-use-preview` | Model capable of controlling a computer interface. | — |
| `gpt-5-codex` | Specialized model for code generation and engineering. | — |
| `codex-mini-latest` | Lightweight model for code generation. | — |
| `web-search` | Tool for grounding responses in live web data. | $10.00 / 1k calls (Content tokens free) |
| `containers` | Secure environments for code execution. | $0.03 per 1GB (Session-based) |

### Deprecated

| Model ID | Replacement | Retirement Date |
| :--- | :--- | :--- |
| `gpt-realtime-mini` | `gpt-realtime-2.1-mini` | — |
| `gpt-4o-mini-tts` | — | — |

## Notes

- **Batch Processing**: Offers a 50% discount on input and output tokens for requests processed asynchronously within 24 hours.
- **Prompt Caching**: Automatically applies to the GPT-5.6 series and Realtime 2.1 models. GPT-5.6 cached input is billed at 10% of standard input: $0.50/$5.00 for Sol, $0.20/$2.00 for Terra, and $0.02/$0.20 for Luna. Cache writes are billed at 1.25x the uncached input rate.
- **Data Residency**: Regional processing and data residency options are available for an additional 10% premium on standard rates.
- **Service Tiers**:
    - **Standard**: Default pay-as-you-go tier.
    - **Priority**: Reliable high-speed performance with flexible pay-as-you-go pricing.
    - **Flex**: Lower cost for non-production tasks in exchange for slower response times and occasional unavailability.
    - **Scale / Reserved Capacity**: Enterprise-grade tiers with SLAs and dedicated throughput.
- **Rate Limits**: Enforced via Usage Tiers (Tier 1 to Tier 5). Limits are model-specific and scale with lifetime spend.
- **Image Tokenization**: Images are converted into tokens for billing. GPT-5.6 and GPT-Realtime use specific image token rates, while older models use standard text token rates based on resolution.
- **Knowledge Cutoff**: The latest GPT-5.6 models have a reliable knowledge cutoff of February 16, 2026.
