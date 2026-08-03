---
provider: Mistral
slug: mistral
last_updated: 2026-08-03T09:55:07Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-08-03T09:55:07Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Multimodal
Frontier-class models optimized for general-purpose conversation, complex reasoning, and multimodal (text/vision) tasks.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-2604` | `mistral-medium-latest`, `mistral-medium-3.5` | text, image | text | 128,000 | 8,192 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision, agentic, coding | Standard, Priority | Input: $1.20<br>Output: $3.60 |
| `mistral-large-2512` | `mistral-large-latest`, `mistral-large-3` | text, image | text | 128,000 | 8,192 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision, multilingual | Standard, Priority | Input: $2.00<br>Output: $6.00 |
| `mistral-small-2603` | `mistral-small-latest`, `mistral-small-4` | text | text | 128,000 | 8,192 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, reasoning, coding | Standard, Priority | Input: $0.20<br>Output: $0.60 |
| `ministral-3-14b-2512` | `ministral-3-14b` | text, image | text | 128,000 | 8,192 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision | Standard | Input: $0.10<br>Output: $0.30 |
| `ministral-3-8b-2512` | `ministral-3-8b` | text, image | text | 128,000 | 8,192 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision | Standard | Input: $0.10<br>Output: $0.30 |
| `ministral-3-3b-2512` | `ministral-3-3b` | text, image | text | 128,000 | 8,192 | — | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision | Standard | Input: $0.04<br>Output: $0.12 |

### Specialized & Coding
Models fine-tuned for specific technical domains like formal proof engineering and high-performance code completion.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `codestral-2508` | `codestral-latest` | text, code | text, code | 32,000 | 4,096 | — | Stable | 80+ code languages | function calling, structured outputs, streaming, FIM (Fill-In-the-Middle) | Standard | Input: $0.20<br>Output: $0.60 |
| `labs-leanstral-1.5` | `leanstral-1.5` | text, code | text, code | 32,000 | 4,096 | — | Experimental | Lean 4 | formal proof engineering, automated theorem proving | Standard | Input: $0.20<br>Output: $0.60 |

### Audio & Speech
Models for audio transcription, live speech processing, and high-fidelity text-to-speech.

| Model ID | Direction | Inputs | Outputs | Languages | Release stage | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `voxtral-mini-transcribe-2602` | STT | audio | text | Multilingual | Stable | $0.006 / minute |
| `voxtral-mini-transcribe-realtime-2602` | STT (Live) | audio | text | Multilingual | Stable | $0.010 / minute |
| `voxtral-tts-2603` | TTS | text | audio | Multilingual | Stable | $0.020 / 1k characters |
| `voxtral-small-2507` | Audio-to-Text | audio, text | text | Multilingual | Stable | Input: $0.20 / MTok<br>Output: $0.60 / MTok |

### Vision & Document AI
Specialized services for extracting structured data and text from documents and images.

| Model ID | Inputs | Output resolution | Capabilities | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-ocr-v4` | image, PDF | Variable | Paragraph-level bounding boxes, structural block labels, LaTeX math extraction | $1.00 / 1,000 pages |
| `mistral-ocr-2512` | image, PDF | Variable | Document AI stack, text extraction | $1.00 / 1,000 pages |

### Embeddings
Semantic representation models for text and code.

| Model ID | Dimensions | Max input | Modalities | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-embed` | 1024 | 8,192 | text | $0.10 |
| `codestral-embed` | 1024 | 8,192 | code, text | $0.10 |

### Specialized

| Model ID | What it does | Pricing |
| :--- | :--- | :--- |
| `mistral-moderation-2603` | Content moderation with jailbreaking detection and 128k context. | $0.06 / MTok |

### Deprecated
Models scheduled for retirement. Users are advised to migrate to the recommended alternatives.

| Model ID | Deprecation Date | Retirement Date | Alternative |
| :--- | :--- | :--- | :--- |
| `labs-leanstral-2603` | 2026-05-21 | 2026-06-29 | `labs-leanstral-1.5` |
| `mistral-medium-2508` | 2026-05-21 | 2026-08-30 | `mistral-medium-2604` |
| `mistral-small-2506` | 2026-04-29 | 2026-07-30 | `mistral-small-2603` |
| `voxtral-mini-2507` | 2026-02-26 | 2026-05-30 | `voxtral-mini-transcribe-2602` |
| `mistral-large-2411` | 2026-02-26 | 2026-05-30 | `mistral-large-2512` |
| `pixtral-large-2411` | 2026-02-26 | 2026-05-30 | `mistral-medium-2604` |
| `mistral-moderation-2411` | 2026-03-30 | 2026-06-29 | `mistral-moderation-2603` |
| `open-mistral-nemo-2407` | 2026-05-21 | 2026-07-30 | `ministral-3-8b-2512` |

## Notes

- **Prompt Caching**: Mistral offers automatic prompt caching for repeated prefixes. Cached tokens are typically billed at a 25% discount compared to standard input tokens.
- **Batch API**: A Batch endpoint is available for non-latency-sensitive workloads, offering a 50% discount on standard token pricing.
- **Free Tier**: Mistral provides a "Free" tier for developers in Studio with limited rate limits (e.g., 1 RPM) for testing and evaluation.
- **Rate Limits**: Limits are tiered based on usage history and billing. Standard Pay-as-you-go (Tier 1) typically starts at 5 requests per second (RPS) and 2M tokens per minute (TPM) for Large models.
- **Regional Options**: Mistral supports data residency in the EU (La Plateforme) and the US. Enterprise customers can request specific regional deployments.
- **Deprecation Policy**: Mistral typically provides a 3-month notice period between deprecation and retirement for major model versions.
- **Fine-tuning**: Fine-tuning is available for `mistral-small`, `mistral-medium`, and `codestral` via the Studio console or API. Pricing is billed per training token plus a hosting fee.
- **License**: Models vary between Apache 2.0 (e.g., `mistral-large-3`, `mistral-small-4`) and "Modified MIT" or "Premier" (e.g., `mistral-medium-3.5`, `codestral`) which may require commercial licenses for high-revenue use cases.
