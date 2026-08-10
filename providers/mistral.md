---
provider: Mistral
slug: mistral
last_updated: 2026-08-10T07:49:39Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-08-10T07:49:39Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Multimodal (Chat & Vision)

These models support both text and image inputs, optimized for general-purpose conversation, reasoning, and agentic workflows.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-latest` | `mistral-medium-2604` | text, image | text | 128,000 | 8,192 | Apr 2026 | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, prompt caching, vision | Moderate | $1.20 (Input)<br>$3.60 (Output) |
| `mistral-large-latest` | `mistral-large-2512`, `mistral-large-3` | text, image | text | 128,000 | 8,192 | Dec 2025 | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, prompt caching, vision, fine-tuning | Moderate | $2.00 (Input)<br>$6.00 (Output) |
| `ministral-3-14b-latest` | `ministral-3-14b-2512` | text, image | text | 128,000 | 8,192 | Dec 2025 | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision | Fast | $0.15 (Input)<br>$0.15 (Output) |
| `ministral-3-8b-latest` | `ministral-3-8b-2512` | text, image | text | 128,000 | 8,192 | Dec 2025 | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision | Fast | $0.10 (Input)<br>$0.10 (Output) |
| `ministral-3-3b-latest` | `ministral-3-3b-2512` | text, image | text | 128,000 | 8,192 | Dec 2025 | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, vision | Fastest | $0.04 (Input)<br>$0.04 (Output) |

### Reasoning & Coding

Models optimized for logic, mathematics, and software engineering.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency / SLA | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-small-latest` | `mistral-small-2603`, `mistral-small-4` | text | text | 128,000 | 8,192 | Mar 2026 | Stable | Multilingual | function calling, structured outputs, streaming, system instructions, reasoning, prompt caching | Fast | $0.20 (Input)<br>$0.60 (Output) |
| `codestral-latest` | `codestral-2508` | text, code | text, code | 32,000 | 4,096 | Aug 2025 | Stable | 80+ | function calling, structured outputs, streaming, system instructions, FIM (Fill-In-the-Middle) | Fast | $0.30 (Input)<br>$0.90 (Output) |
| `leanstral-latest` | `leanstral-1.5` | text, code | text, code | 32,000 | 4,096 | — | Stable | Lean 4 | automated theorem proving, formal proof engineering | Moderate | $0.30 (Input)<br>$0.90 (Output) |

### Audio (Speech & Transcription)

The Voxtral family handles audio-to-text and text-to-audio tasks.

#### Speech-to-Text (STT) & Audio Understanding

| Model ID | Direction | Inputs | Outputs | Context / Max Duration | Languages | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `voxtral-mini-transcribe-2-latest` | Audio -> Text | audio | text | 128,000 tokens | Multilingual | $0.01 per minute |
| `voxtral-mini-transcribe-realtime` | Audio -> Text | audio | text | Live Stream | Multilingual | $0.02 per minute |
| `voxtral-small-latest` | Audio -> Text | audio, text | text | 128,000 tokens | Multilingual | $0.15 / MTok |

#### Text-to-Speech (TTS)

| Model ID | Direction | Inputs | Outputs | Languages | Features | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `voxtral-tts-latest` | Text -> Audio | text | audio | Multilingual | Zero-shot voice cloning | $0.02 per 1k characters |

### Specialized & Moderation

| Model ID | Category | Inputs | Outputs | Description | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-ocr-latest` | OCR | image, PDF | text, JSON | Paragraph-level bounding boxes and structural labels. | $1.00 per 1k pages |
| `shieldstral-latest` | Moderation | text, image | text (labels) | Multimodal safety classification for text and images. | $0.06 / MTok |
| `mistral-moderation-latest` | Moderation | text | text (labels) | Text-only moderation with jailbreak detection. | $0.06 / MTok |
| `mistral-embed-latest` | Embeddings | text | vector (1024) | Semantic representation for RAG and search. | $0.10 / MTok |

### Deprecated

Models in this category are scheduled for retirement. Users should migrate to the recommended alternatives.

| Model ID | Retirement Date | Alternative |
| :--- | :--- | :--- |
| `mistral-medium-2508` | Aug 30, 2026 | `mistral-medium-latest` |
| `mistral-small-2506` | Jul 30, 2026 | `mistral-small-latest` |
| `open-mistral-nemo-2407` | Jul 30, 2026 | `ministral-3-8b-latest` |
| `devstral-2512` | Jul 30, 2026 | `mistral-medium-latest` |
| `labs-leanstral-2603` | Jun 29, 2026 | `leanstral-1.5` |
| `mistral-large-2411` | May 30, 2026 | `mistral-large-latest` |
| `pixtral-large-2411` | May 30, 2026 | `mistral-medium-latest` |
| `voxtral-mini-2507` | May 30, 2026 | `voxtral-mini-transcribe-2-latest` |

## Notes

- **Batch API**: Mistral offers a 25% discount on all models for asynchronous batch processing.
- **Prompt Caching**: Supported on `mistral-large-latest`, `mistral-medium-latest`, and `mistral-small-latest`. Cached tokens are billed at a 50% discount compared to standard input tokens.
- **Rate Limits**: Limits are enforced via Tiers (1-5). Tier 1 (Trial) typically starts at 5 RPM / 20,000 TPM. Tier 5 (Scale) supports up to 2,000 RPM and 2,000,000 TPM depending on the model.
- **Free Tier**: Mistral provides a "Free Tier" on La Plateforme for experimental use with low rate limits on selected open-weight models.
- **Data Residency**: Regional endpoints are available for US and EU customers to ensure data remains within specific jurisdictions.
- **Fine-tuning**: Available for `mistral-large-latest` and `mistral-small-latest` via the La Plateforme dashboard or API.
- **Structured Outputs**: All current chat models support JSON Mode and tool use (function calling) with strict schema enforcement.
- **Context Window**: While the context window is 128,000 tokens for most models, performance is optimized for the first 32,000 tokens in "Small" and "Ministral" variants.
