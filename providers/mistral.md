---
provider: Mistral
slug: mistral
last_updated: 2026-07-27T10:00:03Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-07-27T10:00:03Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models (Generalist)

These are Mistral's high-performance, versatile models designed for a wide range of tasks including reasoning, coding, and multimodal understanding.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mistral-medium-latest` | `mistral-medium-2604` | text, image | text | 128,000 | — | — | Stable | Multilingual | multimodal, agentic, coding, function calling, structured outputs, streaming, system instructions |
| `mistral-small-latest` | `mistral-small-2603` | text | text | 128,000 | — | — | Stable | Multilingual | reasoning, coding, hybrid, function calling, structured outputs, streaming, system instructions |
| `mistral-large-latest` | `mistral-large-2512` | text, image | text | 128,000 | — | — | Stable | Multilingual | multimodal, open-weight, function calling, structured outputs, streaming, system instructions |
| `ministral-3-14b-latest` | `ministral-3-14b-2512` | text, image | text | 128,000 | — | — | Stable | Multilingual | multimodal, vision, function calling, structured outputs, streaming, system instructions |
| `ministral-3-8b-latest` | `ministral-3-8b-2512` | text, image | text | 128,000 | — | — | Stable | Multilingual | multimodal, vision, function calling, structured outputs, streaming, system instructions |
| `ministral-3-3b-latest` | `ministral-3-3b-2512` | text, image | text | 128,000 | — | — | Stable | Multilingual | multimodal, vision, function calling, structured outputs, streaming, system instructions |

| Model ID | Latency tier / SLA | Rate limits | Pricing (Input / Output) |
| :--- | :--- | :--- | :--- |
| `mistral-medium-latest` | Moderate | see Notes | — |
| `mistral-small-latest` | Fast | see Notes | — |
| `mistral-large-latest` | Moderate | see Notes | — |
| `ministral-3-14b-latest` | Fast | see Notes | — |
| `ministral-3-8b-latest` | Fastest | see Notes | — |
| `ministral-3-3b-latest` | Fastest | see Notes | — |

### Specialist Models

Models optimized for specific domains such as software engineering, audio processing, and document intelligence.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `codestral-latest` | `codestral-2508` | text (code) | text | — | — | — | Stable | 80+ code languages | code completion, FIM (Fill-in-the-middle), function calling |
| `devstral-latest` | `devstral-2603` | text (code) | text | — | — | — | Stable | — | code agents, software engineering tasks |
| `mistral-moderation-latest` | `mistral-moderation-2603` | text | text | 128,000 | — | — | Stable | — | jailbreaking detection, safety guardrails |
| `voxtral-mini-transcribe-latest` | `voxtral-mini-transcribe-2602` | audio | text | — | — | — | Stable | — | transcription, efficient audio input |
| `voxtral-mini-transcribe-realtime` | `voxtral-mini-transcribe-realtime-2602` | audio | text | — | — | — | Stable | — | live transcription, low-latency |
| `voxtral-small-latest` | `voxtral-small-2507` | audio | text | — | — | — | Stable | — | audio input for instruct use cases |
| `leanstral-latest` | `labs-leanstral-1.5` | text (code) | text | — | — | — | Experimental | — | Lean 4 formal proof engineering, automated theorem proving |

| Model ID | Latency tier / SLA | Rate limits | Pricing |
| :--- | :--- | :--- | :--- |
| `codestral-latest` | Fast | see Notes | — |
| `devstral-latest` | Moderate | see Notes | — |
| `mistral-moderation-latest` | Fast | see Notes | — |
| `voxtral-mini-transcribe-latest` | Fast | see Notes | — |
| `voxtral-mini-transcribe-realtime` | Fastest | see Notes | — |
| `voxtral-small-latest` | Fast | see Notes | — |
| `leanstral-latest` | Moderate | see Notes | — |

### Audio & Speech Generation

| Model ID | Direction | Supported Languages | Price |
| :--- | :--- | :--- | :--- |
| `voxtral-tts-latest` | text-to-audio | Multilingual | — |

### Document Intelligence (OCR)

| Model ID | Inputs | Output Format | Capabilities | Price |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-ocr-latest` | image, PDF | JSON, Markdown | paragraph-level bounding boxes, structural block labels | — |
| `mistral-ocr-2512` | image, PDF | JSON, Markdown | Document AI stack integration | — |

### Embeddings

| Model ID | Output Dimensions | Max Input Tokens | Supported Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `mistral-embed` | 1024 | 8,192 | text | — |
| `codestral-embed` | — | — | text (code) | — |

### Deprecated / Legacy Models

| Model ID | Alternative | Deprecation Date | Retirement Date |
| :--- | :--- | :--- | :--- |
| `mistral-medium-2508` | `mistral-medium-latest` | 2026-05-21 | 2026-08-30 |
| `mistral-small-2506` | `mistral-small-latest` | 2026-04-29 | 2026-07-30 |
| `mistral-large-2411` | `mistral-medium-latest` | 2026-02-26 | 2026-05-30 |
| `pixtral-large-2411` | `mistral-medium-latest` | 2026-02-26 | 2026-05-30 |
| `open-mistral-nemo-2407` | `ministral-3-8b-latest` | 2026-05-21 | 2026-07-30 |
| `mistral-large-2407` | `mistral-large-latest` | 2024-11-29 | 2025-03-29 |
| `open-mistral-7b` | `ministral-3-8b-latest` | 2024-11-29 | 2025-03-29 |
| `open-mixtral-8x7b` | `mistral-small-latest` | 2024-11-29 | 2025-03-29 |
| `open-mixtral-8x22b` | `mistral-small-latest` | 2024-11-29 | 2025-03-29 |
| `codestral-2405` | `codestral-latest` | 2024-12-01 | 2025-06-15 |
| `mistral-ocr-2505` | `mistral-ocr-latest` | 2026-02-26 | 2026-05-30 |

## Notes

- **Batch API**: Mistral offers a 25% discount for asynchronous batch processing.
- **Prompt Caching**: Supported on frontier models; reduces costs for repeated prefixes in long-context conversations.
- **Free Tier**: Mistral "La Plateforme" provides a free tier for experimentation with limited rate limits.
- **Rate Limits**: Limits are tiered based on usage history and billing (Free, Tier 1, Tier 2, Tier 3, Tier 4). Specific RPM/TPM caps vary by model and tier.
- **Data Residency**: Mistral offers regional deployments, including EU-hosted servers for GDPR compliance.
- **Deprecation Policy**: Models typically have a 3-6 month window between deprecation announcement and final retirement.
- **Tooling**: Mistral provides "Studio" for agent orchestration, "Forge" for model customization, and "Vibe" for autonomous long-horizon tasks.
- **Pricing Sources**: Detailed pricing and rate limit tables were unreachable at the time of this update; refer to the official pricing page for the latest USD rates.
