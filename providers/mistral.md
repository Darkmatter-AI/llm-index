---
provider: Mistral
slug: mistral
last_updated: 2026-07-06T07:45:11Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-07-06T07:45:11Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Generalist (Frontier)

Mistral's frontier models are high-performance multimodal models optimized for a broad range of tasks, including agentic workflows, reasoning, and coding.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing ($/MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-2604` | `mistral-medium-latest` | text, image | text | 128,000 | 8,192 | — | Stable | 80+ | multimodal, function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $2.00<br>Output: $6.00 |
| `mistral-small-2603` | `mistral-small-latest` | text | text | 128,000 | 8,192 | — | Stable | 80+ | function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $0.20<br>Output: $0.60 |
| `mistral-large-2512` | `mistral-large-latest` | text, image | text | 128,000 | 8,192 | — | Stable | 80+ | multimodal, function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $2.00<br>Output: $6.00 |
| `ministral-3-14b-2512` | `ministral-14b-latest` | text, image | text | 128,000 | 8,192 | — | Stable | 80+ | multimodal, function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $0.15<br>Output: $0.15 |
| `ministral-3-8b-2512` | `ministral-8b-latest` | text, image | text | 128,000 | 8,192 | — | Stable | 80+ | multimodal, function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $0.10<br>Output: $0.10 |
| `ministral-3-3b-2512` | `ministral-3b-latest` | text, image | text | 128,000 | 8,192 | — | Stable | 80+ | multimodal, function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $0.04<br>Output: $0.04 |

### Specialist

Specialized models optimized for specific domains such as coding, mathematics, transcription, and moderation.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing ($/MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `codestral-2508` | `codestral-latest` | text, code | text, code | 32,000 | 8,192 | — | Stable | 80+ | function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $0.20<br>Output: $0.60 |
| `devstral-2604` | `devstral-latest` | text, code | text, code | 128,000 | 8,192 | — | Stable | 80+ | function calling, structured outputs, streaming, system instructions, caching, batch | Standard | Input: $2.00<br>Output: $6.00 |
| `mistral-moderation-2603` | `mistral-moderation-latest` | text | text | 128,000 | 8,192 | — | Stable | 80+ | moderation, jailbreaking detection | Standard | $0.06 per MTok |
| `voxtral-mini-transcribe-2602` | `voxtral-mini-transcribe-latest` | audio | text | — | — | — | Stable | Multilingual | transcription, live transcription | Standard | — |
| `voxtral-small-2507` | — | audio | text | — | — | — | Stable | Multilingual | audio input, instruct | Standard | — |
| `leanstral-1.5` | `labs-leanstral-1.5` | text, code | text, code | — | — | — | Labs | — | formal proof engineering, theorem proving | Standard | — |

### Speech & Audio

| Model ID | Direction | Supported Languages | Pricing |
| :--- | :--- | :--- | :--- |
| `voxtral-tts-2603` | Text-to-Speech | Multilingual | — |
| `voxtral-mini-transcribe-realtime` | Audio-to-Text | Multilingual | — |

### Embeddings

| Model ID | Output Dimensions | Max Input Tokens | Supported Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-embed-2312` | 1024 | 8,192 | text | $0.10 |
| `codestral-embed-2505` | — | — | code | — |

### Specialized Services

| Model ID | Description | Pricing |
| :--- | :--- | :--- |
| `mistral-ocr-v4` | Latest OCR service with paragraph-level bounding boxes and structural block labels. | — |
| `mistral-ocr-v25.12` | OCR service powering Document AI stack. | — |

### Deprecated

| Model ID | Alternative | Deprecation Date | Retirement Date |
| :--- | :--- | :--- | :--- |
| `labs-leanstral-2603` | `leanstral-1.5` | 2026-05-21 | 2026-06-29 |
| `mistral-medium-2508` | `mistral-medium-3.5` | 2026-05-21 | 2026-08-30 |
| `mistral-small-2506` | `mistral-small-4` | 2026-04-29 | 2026-07-30 |
| `devstral-2512` | `mistral-medium-3.5` | 2026-05-21 | 2026-07-30 |
| `magistral-medium-2509` | `mistral-medium-3.5` | 2026-05-21 | 2026-07-30 |
| `magistral-small-2509` | `mistral-small-4` | 2026-04-30 | 2026-07-31 |
| `mistral-large-2411` | `mistral-medium-3.5` | 2026-02-26 | 2026-05-30 |
| `pixtral-large-2411` | `mistral-medium-3.5` | 2026-02-26 | 2026-05-30 |
| `mistral-moderation-2411` | `mistral-moderation-2` | 2026-03-30 | 2026-06-29 |
| `ministral-3b-2410` | `ministral-3-3b` | 2025-12-01 | 2025-12-30 |
| `ministral-8b-2410` | `ministral-3-8b` | 2025-12-01 | 2025-12-30 |
| `mistral-small-2409` | `mistral-small-4` | 2025-11-05 | 2025-11-29 |
| `pixtral-12b-2409` | `ministral-3-14b` | 2025-12-01 | 2025-12-30 |
| `mistral-large-2407` | `mistral-large-3` | 2024-11-29 | 2025-03-29 |
| `open-mistral-nemo-2407` | `ministral-3-8b` | 2026-05-21 | 2026-07-30 |
| `codestral-2405` | `codestral` | 2024-12-01 | 2025-06-15 |
| `open-mistral-7b` | `ministral-3-8b` | 2024-11-29 | 2025-03-29 |
| `open-mixtral-8x22b` | `mistral-small-4` | 2024-11-29 | 2025-03-29 |
| `open-mixtral-8x7b` | `mistral-small-4` | 2024-11-29 | 2025-03-29 |

## Notes

- **Batch API:** Mistral offers a Batch API for asynchronous processing with a **25% discount** compared to synchronous API pricing.
- **Prompt Caching:** Automatically caches repeated prefixes in prompts. Cached input tokens are billed at a **50% discount** ($0.5x the standard input rate).
- **Free Tier:** Mistral provides a free trial tier on "La Plateforme" with limited rate limits for testing and development.
- **Regional Options:** Data residency is supported in the EU (via La Plateforme) and globally through partners like Azure, AWS (Bedrock), and Google Cloud (Vertex AI).
- **Rate Limits:** Limits are tiered based on usage and billing history (Tier 1 to Tier 5). Typical Tier 1 limits are 100 RPM and 200k TPM per model.
- **Fine-tuning:** Supported for `mistral-small-latest`, `mistral-large-latest`, and `open-mistral-7b`. Pricing is typically billed per token for training and a hosting fee.
- **Multilingual Support:** Frontier models support 80+ languages, including English, French, German, Spanish, Italian, Chinese, Japanese, Korean, Portuguese, and Arabic.
- **Structured Outputs:** Supported via `response_format: { "type": "json_object" }` or JSON Schema for most models.
