---
provider: Mistral
slug: mistral
last_updated: 2026-06-22T08:17:54Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-06-22T08:17:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models (Generalist)

Versatile, high-performing models suitable for a broad range of tasks, including text and vision processing.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (Input/Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-2604` | `mistral-medium-latest` | text, image | text | — | — | — | Stable | — | multimodal, agentic, coding, function calling, structured outputs, streaming, system instructions | Standard | — |
| `mistral-small-2603` | `mistral-small-latest` | text | text | — | — | — | Stable | — | reasoning, instruct, coding, function calling, structured outputs, streaming, system instructions | Standard | — |
| `mistral-large-2512` | `mistral-large-latest` | text, image | text | — | — | — | Stable | — | multimodal, general-purpose, function calling, structured outputs, streaming, system instructions | Standard | — |
| `ministral-3-14b-2512` | — | text, image | text | — | — | — | Stable | — | vision, text, function calling, structured outputs, streaming, system instructions | Standard | — |
| `ministral-3-8b-2512` | — | text, image | text | — | — | — | Stable | — | vision, text, function calling, structured outputs, streaming, system instructions | Standard | — |
| `ministral-3-3b-2512` | — | text, image | text | — | — | — | Stable | — | vision, text, function calling, structured outputs, streaming, system instructions | Standard | — |

### Specialist Models

Models optimized for specific domains such as coding, OCR, or moderation.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Pricing (Input/Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `codestral-2508` | `codestral-latest` | text, code | text, code | — | — | — | Stable | — | code completion, function calling, structured outputs, streaming, system instructions | Standard | — |
| `devstral-2-2512` | — | text, code | text, code | — | — | — | Stable | — | code agents, software engineering tasks, function calling, structured outputs, streaming | Standard | — |
| `ocr-3-2512` | `mistral-ocr-latest` | image, PDF | text, JSON | — | — | — | Stable | — | OCR, document understanding, structured outputs | Standard | — |
| `mistral-moderation-2603` | `mistral-moderation-latest` | text | text | 128,000 | — | — | Stable | Multilingual | jailbreaking detection, multilingual moderation, structured outputs | Standard | — |

### Audio Models

Models designed for speech-to-text (STT), text-to-speech (TTS), and audio understanding.

| Model ID | Direction | Supported Languages | Release stage | Capabilities | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `voxtral-tts-2603` | text-to-audio | Multilingual | Stable | zero-shot voice cloning, multilingual support | — |
| `voxtral-mini-transcribe-2602` | audio-to-text | — | Stable | transcription, audio input | — |
| `voxtral-mini-transcribe-realtime-2602` | audio-to-text | — | Stable | live transcription, realtime audio API | — |
| `voxtral-small-2507` | audio-to-text | — | Stable | audio input for instruct use cases | — |

### Embeddings

| Model ID | Output Dimensions | Max Input Tokens | Supported Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-embed-2312` | — | — | text | — |
| `codestral-embed-2505` | — | — | code, text | — |

### Deprecated Models

Models that have been superseded and are scheduled for retirement.

| Model ID | Retirement Date | Alternative |
| :--- | :--- | :--- |
| `labs-leanstral-2603` | June 30, 2026 | — |
| `mistral-medium-2508` | August 31, 2026 | `mistral-medium-2604` |
| `mistral-small-2506` | July 31, 2026 | `mistral-small-2603` |
| `devstral-2512` | July 31, 2026 | `mistral-medium-2604` |
| `magistral-medium-2509` | July 31, 2026 | `mistral-medium-2604` |
| `magistral-small-2509` | July 31, 2026 | `mistral-small-2603` |
| `mistral-medium-2505` | August 31, 2026 | `mistral-medium-2604` |
| `mistral-moderation-2411` | June 30, 2026 | `mistral-moderation-2603` |
| `open-mistral-nemo-2407` | July 31, 2026 | `ministral-3-8b-2512` |
| `mistral-large-2411` | May 31, 2026 | `mistral-medium-2604` |
| `pixtral-large-2411` | May 31, 2026 | `mistral-medium-2604` |
| `voxtral-mini-2507` | May 31, 2026 | `voxtral-mini-transcribe-2602` |
| `devstral-medium-2507` | May 31, 2026 | `mistral-medium-2604` |
| `devstral-small-2507` | May 31, 2026 | `mistral-small-2603` |
| `mistral-ocr-2505` | May 31, 2026 | `ocr-3-2512` |

## Notes

- **Prompt Caching**: Mistral supports prompt caching for repeated context. Cached tokens are typically billed at a discounted rate, though exact 2026 pricing is not published in the overview.
- **Rate Limit Tiers**: Mistral uses a tiered system (Free, Tier 1, Tier 2, Tier 3, Tier 4) based on usage and payment history. Limits are applied per model and per tier.
- **Regional Availability**: Models are available via Mistral's La Plateforme and through cloud partners including AWS (Bedrock), Azure (AI Studio), GCP (Vertex AI), and IBM.
- **Data Residency**: Mistral offers regional endpoints to comply with data residency requirements, particularly for European customers.
- **Fine-tuning**: Fine-tuning is available for select models (e.g., Mistral Small, Mistral NeMo) via the Mistral API.
- **Vibe Platform**: Mistral's "Vibe" product serves as a unified agent for productivity and coding, utilizing the latest frontier models.
- **Organization Management**: Organization setup, billing, SSO, and Workspaces are managed through the Admin Panel.
- **Deprecation Policy**: Mistral typically provides a deprecation period of several months before a model is retired, as seen in the retirement schedule for 2024-2025 models.
