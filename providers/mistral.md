---
provider: Mistral
slug: mistral
last_updated: 2026-07-20T09:24:02Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-07-20T09:24:02Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Generalist
Versatile, high-performing models suitable for a broad range of tasks including text generation, reasoning, and multimodal understanding.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-latest` | `mistral-medium-2604` | text, image | text | 128,000 | 8,192 | — | Stable | — |
| `mistral-small-latest` | `mistral-small-2603` | text | text | 128,000 | 8,192 | — | Stable | — |
| `mistral-large-latest` | `mistral-large-2512` | text, image | text | 128,000 | 8,192 | — | Stable | — |
| `ministral-3b-latest` | `ministral-3b-2512` | text, image | text | 128,000 | 8,192 | — | Stable | — |
| `ministral-8b-latest` | `ministral-8b-2512` | text, image | text | 128,000 | 8,192 | — | Stable | — |
| `ministral-14b-latest` | `ministral-14b-2512` | text, image | text | 128,000 | 8,192 | — | Stable | — |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output) |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-latest` | multimodal, function calling, structured outputs, streaming, system instructions | Moderate | see Notes | $2.0 / $6.0 per MTok |
| `mistral-small-latest` | reasoning, function calling, structured outputs, streaming, system instructions | Fast | see Notes | $0.2 / $0.6 per MTok |
| `mistral-large-latest` | multimodal, function calling, structured outputs, streaming, system instructions | Moderate | see Notes | $2.0 / $6.0 per MTok |
| `ministral-3b-latest` | multimodal, function calling, structured outputs, streaming, system instructions | Fastest | see Notes | $0.04 / $0.04 per MTok |
| `ministral-8b-latest` | multimodal, function calling, structured outputs, streaming, system instructions | Fastest | see Notes | $0.1 / $0.1 per MTok |
| `ministral-14b-latest` | multimodal, function calling, structured outputs, streaming, system instructions | Fast | see Notes | $0.15 / $0.15 per MTok |

### Specialized
Models optimized for specific domains such as coding, mathematics, or formal proof engineering.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `codestral-latest` | `codestral-2508` | text, code | text | 32,000 | 8,192 | — | Stable |
| `devstral-latest` | `devstral-2602` | text, code | text | 128,000 | 8,192 | — | Stable |
| `leanstral-latest` | `labs-leanstral-1.5` | text, code | text | 128,000 | 8,192 | — | Experimental |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output) |
| :--- | :--- | :--- | :--- | :--- |
| `codestral-latest` | function calling, structured outputs, streaming, system instructions, FIM | Fast | see Notes | $0.2 / $0.6 per MTok |
| `devstral-latest` | code agents, function calling, structured outputs, streaming | Moderate | see Notes | — |
| `leanstral-latest` | formal proof engineering, automated theorem proving | Moderate | see Notes | — |

### Audio & Speech
Models designed for transcription, translation, and text-to-speech generation.

| Model ID | Direction | Languages | Release stage | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `voxtral-tts-latest` | text-to-audio | Multilingual | Stable | — |
| `voxtral-mini-transcribe-latest` | audio-to-text | — | Stable | — |
| `voxtral-mini-transcribe-realtime` | audio-to-text | — | Stable | — |
| `voxtral-small-latest` | audio-to-text | — | Stable | — |

### Specialized Services
Models for document processing and content moderation.

| Model ID | Function | Inputs | Context window | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-ocr-latest` | Document AI / OCR | image, PDF | — | — |
| `mistral-moderation-latest` | Content Moderation | text | 128,000 | — |

### Embeddings
Models for semantic representation of text and code.

| Model ID | Dimensions | Max input tokens | Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-embed` | 1024 | 8,192 | text | $0.1 |
| `codestral-embed` | — | 32,000 | text, code | — |

### Deprecated
Models scheduled for retirement.

| Model ID | Alternative | Deprecation Date | Retirement Date |
| :--- | :--- | :--- | :--- |
| `mistral-medium-2508` | `mistral-medium-latest` | 2026-05-21 | 2026-08-30 |
| `mistral-small-2506` | `mistral-small-latest` | 2026-04-29 | 2026-07-30 |
| `mistral-large-2411` | `mistral-large-latest` | 2026-02-26 | 2026-05-30 |
| `pixtral-large-2411` | `mistral-medium-latest` | 2026-02-26 | 2026-05-30 |
| `ministral-3b-2410` | `ministral-3b-latest` | 2025-12-01 | 2025-12-30 |
| `ministral-8b-2410` | `ministral-8b-latest` | 2025-12-01 | 2025-12-30 |
| `pixtral-12b-2409` | `ministral-14b-latest` | 2025-12-01 | 2025-12-30 |
| `open-mistral-nemo-2407` | `ministral-8b-latest` | 2026-05-21 | 2026-07-30 |

## Notes

- **Rate Limits**: Mistral uses a tiered system (Tier 1 to Tier 5). Tier 1 starts at 5 RPS / 200k TPM. Tier 5 reaches up to 100 RPS / 20M TPM.
- **Prompt Caching**: Supported on latest models. Cached input is typically billed at a 50% discount compared to standard input.
- **Batch API**: Offers a 50% discount on standard pricing for asynchronous processing.
- **Free Tier**: Available via "Mistral La Plateforme" for testing and evaluation with lower rate limits.
- **Regional Options**: Data residency options are available for Enterprise customers in EU and US regions.
- **Fine-tuning**: Supported for `mistral-small-latest` and `open-mistral-7b`.
- **Structured Outputs**: All latest models support JSON mode and function calling.
- **Vision Support**: Multimodal models (Medium 3.5, Large 3, Ministral 3) accept images via the standard chat completion interface.
