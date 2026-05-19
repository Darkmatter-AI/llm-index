---
provider: Mistral
slug: mistral
last_updated: 2026-05-19T12:31:46Z
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · **Mistral**

# Mistral

**Sources:** [docs.mistral.ai/getting-started/models/models_overview](https://docs.mistral.ai/getting-started/models/models_overview/)  ·  **Updated:** `2026-05-19T12:31:46Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Mistral Large 3` | v25.12 | text, image | text | — | — | — | Stable | — | multimodal | — | see Notes | — |
| `Devstral 2` | v25.12 | code | text | — | — | — | Stable | — | code generation | — | see Notes | — |
| `Mistral Medium 3.5` | v3.5 | text, image | text | — | — | — | Stable | — | multimodal, coding | — | see Notes | — |
| `Mistral Small 4` | v26.03 | text | text | — | — | — | Stable | — | instruct, reasoning, coding | — | see Notes | — |
| `Mistral Medium 3.1` | v25.08 | text, image | text | — | — | — | Preview | — | multimodal | — | see Notes | — |
| `Ministral 3 14B` | v25.12 | text, image | text | — | — | — | Stable | — | vision | — | see Notes | — |
| `Ministral 3 8B` | v25.12 | text, image | text | — | — | — | Stable | — | vision | — | see Notes | — |
| `Ministral 3 3B` | v25.12 | text, image | text | — | — | — | Stable | — | vision | — | see Notes | — |
| `Magistral Medium 1.2` | v25.09 | text, image | text | — | — | — | Preview | — | multimodal, reasoning | — | see Notes | — |

### Specialist Models

| Model ID | Description | Inputs | Outputs | Release stage |
| :--- | :--- | :--- | :--- | :--- |
| `Voxtral TTS` | Text-to-speech with zero-shot voice cloning and multilingual support. | text | audio | Stable |
| `Leanstral` | Open-source code agent for Lean 4 formal proof engineering. | code | text | Experimental |
| `OCR 3` | OCR service for Document AI. | image | text | Preview |
| `Voxtral Mini Transcribe 2` | Speech-to-text optimized for transcription. | audio | text | Preview |
| `Voxtral Mini Transcribe Realtime` | Speech-to-text optimized for live transcription. | audio | text | Stable |
| `Codestral` | Language model for code completion. | code | text | Preview |
| `Voxtral Small` | Model with audio input capabilities for instruct use cases. | audio | text | Stable |
| `Mistral Moderation 2` | Moderation model with 128k context window and jailbreaking detection. | text | text | Preview |

### Embedding Models

| Model ID | Description | Inputs | Output Dimensions | Max Input Tokens |
| :--- | :--- | :--- | :--- | :--- |
| `Codestral Embed` | Semantic representation for code extracts. | code | — | — |
| `Mistral Embed` | Semantic representation for code extracts. | code | — | — |

### Other Models

| Model ID | Aliases / snapshots | Inputs | Outputs | Release stage |
| :--- | :--- | :--- | :--- | :--- |
| `Mistral Medium 3` | v25.05 | text, image | text | Preview |
| `Mistral Nemo 12B` | v24.07 | text | text | Stable |

### Deprecated Models

| Model ID | API ID | Deprecation Date | Retirement Date | Alternative |
| :--- | :--- | :--- | :--- | :--- |
| `Mistral Small 3.2` | `mistral-small-2506` | Apr 30, 2026 | Jul 31, 2026 | `Mistral Small 4` |
| `Magistral Medium 1.1` | `magistral-medium-2507` | Oct 31, 2025 | Nov 30, 2025 | `Magistral Medium 1.2` |
| `Mistral Small Creative` | `labs-mistral-small-creative` | Mar 31, 2026 | Apr 30, 2026 | `Mistral Nemo 12B` |
| `Devstral Small 2` | `labs-devstral-small-2512` | Feb 27, 2026 | Mar 31, 2026 | `Devstral 2` |
| `Magistral Small 1.2` | `magistral-small-2509` | Apr 30, 2026 | Jul 31, 2026 | `Mistral Small 4` |
| `Magistral Small 1.1` | `magistral-small-2507` | Oct 31, 2025 | Nov 30, 2025 | `Magistral Small 1.2` |
| `Voxtral Mini` | `voxtral-mini-2507` | Feb 27, 2026 | May 31, 2026 | `Voxtral Mini Transcribe 2` |
| `Devstral Medium 1.0` | `devstral-medium-2507` | Feb 27, 2026 | May 31, 2026 | `Devstral 2` |
| `Devstral Small 1.1` | `devstral-small-2507` | Feb 27, 2026 | May 31, 2026 | `Devstral 2` |
| `Magistral Medium 1.0` | `magistral-medium-2506` | Oct 31, 2025 | Nov 30, 2025 | `Magistral Medium 1.2` |
| `Magistral Small 1.0` | `magistral-small-2506` | Oct 31, 2025 | Nov 30, 2025 | `Magistral Small 1.2` |
| `OCR 2` | `mistral-ocr-2505` | Feb 27, 2026 | May 31, 2026 | `OCR 3` |
| `Devstral Small 1.0` | `devstral-small-2505` | Oct 31, 2025 | Nov 30, 2025 | `Devstral Small 2` |
| `Mistral Small 3.1` | `mistral-small-2503` | Nov 6, 2025 | Nov 30, 2025 | `Mistral Small 3.2` |
| `OCR` | `mistral-ocr-2503` | Dec 2, 2025 | Dec 31, 2025 | `OCR 3` |
| `Mistral Saba` | `mistral-saba-2502` | Jun 10, 2025 | Sep 30, 2025 | `Mistral Small 3.2` |
| `Mistral Small 3.0` | `mistral-small-2501` | Nov 6, 2025 | Nov 30, 2025 | `Mistral Small 3.2` |
| `Codestral` | `codestral-2501` | Nov 6, 2025 | Nov 30, 2025 | `Codestral` |
| `Mistral Large 2.1` | `mistral-large-2411` | Feb 27, 2026 | May 31, 2026 | `Mistral Large 3` |
| `Pixtral Large` | `pixtral-large-2411` | Feb 27, 2026 | May 31, 2026 | `Mistral Large 3` |
| `Mistral Moderation` | `mistral-moderation-2411` | Mar 31, 2026 | Jun 30, 2026 | `Mistral Moderation 2` |
| `Ministral 3B` | `ministral-3b-2410` | Dec 2, 2025 | Dec 31, 2025 | `Ministral 3 3B` |
| `Ministral 8B` | `ministral-8b-2410` | Dec 2, 2025 | Dec 31, 2025 | `Ministral 3 8B` |
| `Mistral Small 2.0` | `mistral-small-2409` | Nov 6, 2025 | Nov 30, 2025 | `Mistral Small 3.2` |
| `Pixtral 12B` | `pixtral-12b-2409` | Dec 2, 2025 | Dec 31, 2025 | `Ministral 3 14B` |
| `Mistral Large 2.0` | `mistral-large-2407` | Nov 30, 2024 | Mar 30, 2025 | `Mistral Large 3` |
| `Codestral Mamba 7B` | `open-codestral-mamba` | Jun 6, 2025 | Jun 6, 2025 | `Codestral` |
| `Codestral` | `codestral-2405` | Dec 2, 2024 | Jun 16, 2025 | `Codestral` |
| `Mistral 7B` | `open-mistral-7b` | Nov 30, 2024 | Mar 30, 2025 | `Ministral 3 8B` |
| `Mixtral 8x22B` | `open-mixtral-8x22b` | Nov 30, 2024 | Mar 30, 2025 | `Mistral Small 3.2` |
| `Mistral Small 1.0` | `mistral-small-2402` | Nov 30, 2024 | Jun 16, 2025 | `Mistral Small 3.2` |
| `Mistral Large 1.0` | `mistral-large-2402` | Nov 30, 2024 | Jun 16, 2025 | `Mistral Large 3` |
| `Mistral Medium 1.0` | `mistral-medium-2312` | Nov 30, 2024 | Jun 16, 2025 | `Mistral Medium 3.1` |
| `Mixtral 8x7B` | `open-mixtral-8x7b` | Nov 30, 2024 | Mar 30, 2025 | `Mistral Small 3.2` |

## Notes

*   **Model Tiers**: Models are designated as "Premier", "Open", or "Labs", but the specific implications of these tiers are not detailed in the overview documentation.
*   **Model Naming**: Model versions are included in the name, for example, `v26.03` for `Mistral Small 4`.
*   **API IDs**: For deprecated models, a specific API ID (e.g., `mistral-small-2506`) is listed. These are not provided for current models in the overview.
*   **Rate Limits**: Per-model rate limit information is not available in the models overview.
*   **Pricing**: Detailed pricing information is not available in the models overview.
