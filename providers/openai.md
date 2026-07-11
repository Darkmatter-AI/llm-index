---
provider: OpenAI
slug: openai
last_updated: 2026-07-11T07:21:58Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
  - https://openai.com/index/previewing-gpt-5-6-sol/
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [openai.com/api/pricing](https://openai.com/api/pricing/), [platform.openai.com/docs/models](https://platform.openai.com/docs/models)  ·  **Updated:** `2026-07-11T07:21:58Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier Models (GPT-5 Series)

The GPT-5 series represents the latest generation of flagship models, with gpt-5.6-sol as the flagship, optimized for complex reasoning, coding, and professional workflows. All models in this series support text and image input, text output, and vision capabilities.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | — | text, image | text | 1,050,000 | 128,000 | Feb 2026 | Stable | — | reasoning, streaming, function calling, structured outputs, web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP, tool search, vision | Standard, Priority, Batch, Flex | Input: $5.00<br>Cached: $0.50<br>Output: $30.00 |
| `gpt-5.6-terra` | — | text, image | text | 1,050,000 | 128,000 | Feb 2026 | Stable | — | reasoning, streaming, function calling, structured outputs, web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP, tool search, vision | Standard, Priority, Batch, Flex | Input: $2.50<br>Cached: $0.25<br>Output: $15.00 |
| `gpt-5.6-luna` | — | text, image | text | 1,050,000 | 128,000 | Feb 2026 | Stable | — | reasoning, streaming, function calling, structured outputs, web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP, tool search, vision | Standard, Priority, Batch, Flex | Input: $1.00<br>Cached: $0.10<br>Output: $6.00 |
| `gpt-5.5` | `gpt-5.5-latest` | text, image, audio, video, code | text, audio, image | 1,000,000 | 128,000 | Dec 2025 | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, file search, web search, computer use, vision, multilingual | Standard, Priority, Batch, Flex | Input: $5.00<br>Cached: $0.50<br>Output: $30.00 |
| `gpt-5.4` | `gpt-5.4-latest` | text, image, audio, video, code | text, audio, image | 1,000,000 | 128,000 | Aug 2025 | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, file search, web search, computer use, vision, multilingual | Standard, Priority, Batch, Flex | Input: $2.50<br>Cached: $0.25<br>Output: $15.00 |
| `gpt-5.4-mini` | `gpt-5.4-mini-latest` | text, image, audio, video, code | text, audio, image | 400,000 | 128,000 | Aug 2025 | Stable | — | function calling, structured outputs, streaming, system instructions, caching, batch, code execution, file search, web search, computer use, vision, multilingual | Faster | Input: $0.75<br>Cached: $0.075<br>Output: $4.50 |
| `gpt-5.4-nano` | — | text, image | text | — | — | Aug 2025 | Stable | — | vision, multilingual | Fastest | — |
| `gpt-5.6` | — | — | — | — | — | — | Preview | — | — | — | — |
| `gpt-5` | — | text, image | text | — | — | — | Stable | — | vision, tools | — | — |
| `gpt-5.1` | — | text, image | text | — | — | — | Stable | — | vision, tools | — | — |
| `gpt-5.2` | — | text, image | text | — | — | — | Stable | — | vision, tools | — | — |

### Reasoning Models (o Series)

Reasoning models are designed to spend more time thinking before producing a response, making them ideal for complex, multi-step problems and STEM use cases.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `o3` | — | text, image | text | — | — | Oct 2023 | Stable | — | reasoning, function calling, structured outputs, vision | Standard, Priority | — |
| `o3-deep-research` | — | text, image | text | — | — | — | Stable | — | reasoning, web search, file search | — | — |
| `o3-pro-2025-06-10` | — | text, image | text | — | — | — | Stable | — | reasoning, tools | Priority | — |
| `o4-mini` | — | text, image | text | — | — | — | Stable | — | reasoning, vision | Faster | — |
| `o4-mini-deep-research` | — | text, image | text | — | — | — | Stable | — | reasoning, web search | — | — |
| `o1` | `o1-2024-12-17` | text, image | text | 128,000 | 32,768 | Oct 2023 | Stable | — | reasoning, function calling, structured outputs, vision | Standard | Input: $15.00<br>Cached: $7.50<br>Output: $60.00 |
| `o1-pro` | — | text, image | text | 128,000 | 32,768 | Oct 2023 | Stable | — | reasoning, function calling, structured outputs, vision | Priority | — |
| `o1-mini` | `o1-mini-2024-09-12` | text | text | 128,000 | 65,536 | Oct 2023 | Stable | — | reasoning, function calling, structured outputs | Faster | Input: $1.10<br>Cached: $0.55<br>Output: $4.40 |

### Multimodal / Chat Models (GPT-4o Series)

The GPT-4o series provides high-performance multimodal capabilities across text and vision.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages | Capabilities | Latency Tier / SLA | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-4o` | `gpt-4o-2024-05-13`, `gpt-4o-latest` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable | — | function calling, structured outputs, streaming, vision | Standard | Input: $5.00<br>Cached: $2.50<br>Output: $15.00 |
| `gpt-4o-mini` | `gpt-4o-mini-latest` | text, image | text | 128,000 | 16,384 | Oct 2023 | Stable | — | function calling, structured outputs, streaming, vision | Faster | Input: $0.15<br>Cached: $0.075<br>Output: $0.60 |
| `gpt-4.1` | — | text, image | text | — | — | — | Stable | — | vision | — | — |
| `gpt-4.1-mini` | — | text, image | text | — | — | — | Stable | — | vision | — | — |
| `gpt-4.1-nano` | — | text, image | text | — | — | — | Stable | — | vision | — | — |
| `gpt-4.5-preview` | — | text, image | text | — | — | — | Preview | — | vision | — | — |

### Realtime Models

Models optimized for low-latency, streaming interactions involving audio, text, and images.

| Model ID | Inputs | Outputs | Context Window | Max Output | Release Stage | Capabilities | Pricing (per 1M tokens) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2` | text, audio, image | text, audio | — | — | Stable | live API, audio generation, vision | Audio Input: $32.00<br>Audio Cached: $0.40<br>Audio Output: $64.00<br>Text Input: $4.00<br>Text Cached: $0.40<br>Text Output: $24.00<br>Image Input: $5.00<br>Image Cached: $0.50 |
| `gpt-realtime-1.5` | text, audio | text, audio | — | — | Stable | live API, audio generation | — |
| `gpt-realtime-mini` | text, audio | text, audio | — | — | Stable | live API, audio generation | — |

### Image Generation

| Model ID | Inputs | Output Resolution | Price per Image / Token | Batch Discount |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-image-2` | text, image | — | Image Input: $8.00 / 1M tokens<br>Image Cached: $2.00 / 1M tokens<br>Image Output: $30.00 / 1M tokens<br>Text Input: $5.00 / 1M tokens<br>Text Cached: $1.25 / 1M tokens | 50% |
| `dall-e-3` | text | 1024x1024, 1024x1792 | $0.040 / image (Standard)<br>$0.080 / image (HD) | — |
| `dall-e-2` | text, image+mask | 256x256, 512x512, 1024x1024 | $0.016 - $0.020 / image | — |

### Speech / TTS / STT

| Model ID | Direction | Languages | Price |
| :--- | :--- | :--- | :--- |
| `gpt-realtime-translate` | Speech-to-Speech | — | $0.034 / minute ($0.00057 / second) |
| `gpt-realtime-whisper` | Speech-to-Text | — | $0.017 / minute ($0.00028 / second) |
| `gpt-4o-transcribe` | Speech-to-Text | — | — |
| `gpt-4o-mini-transcribe` | Speech-to-Text | — | — |
| `whisper-1` | Speech-to-Text | 50+ | $0.006 / minute |
| `tts-1` / `tts-1-hd` | Text-to-Speech | — | $15.00 - $30.00 / 1M characters |

### Embeddings

| Model ID | Dimensions | Max Input | Modalities | Price per MTok |
| :--- | :--- | :--- | :--- | :--- |
| `text-embedding-3-small` | 1536 (reducible) | 8,191 | text | $0.02 |
| `text-embedding-3-large` | 3072 (reducible) | 8,191 | text | $0.13 |
| `text-embedding-ada-002` | 1536 | 8,191 | text | $0.10 |

### Specialized & Tools

| Model ID | Description | Pricing |
| :--- | :--- | :--- |
| `computer-use-preview` | Model capable of controlling a computer interface. | — |
| `web-search` | Tool for grounding responses with up-to-date web info. | $10.00 / 1k calls (Search content tokens are free) |
| `containers` | Secure environments for code execution. | $0.03 / 1GB (Starting March 31, 2026: per 20-minute session) |
| `omni-moderation-latest` | Multimodal moderation for text and images. | Free for most use cases |
| `codex-mini-latest` | Optimized model for code generation. | — |
| `gpt-5-codex` | Flagship code generation model. | — |

### Deprecated

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `gpt-4o-mini-tts` | — | — |
| `gpt-3.5-turbo` | — | `gpt-4o-mini` |

## Notes

- **GPT-5.6 naming:** The number identifies the generation, while Sol, Terra, and Luna are durable capability tiers. Each tier also has a `-fast` serving variant at approximately 1.5x speed.
- **Batch API:** Offers a 50% discount on input and output tokens for tasks submitted via the batch endpoint. Tasks are typically completed within 24 hours.
- **Prompt Caching:** Automatically applied to input prefixes that match recently used prompts. For the GPT-5 series, cached input is billed at 10% of the standard input rate.
- **Data Residency:** Regional processing and data residency options are available for an additional 10% premium on standard rates.
- **Service Tiers:** OpenAI offers multiple tiers including Standard, Priority (guaranteed high-speed), Flex (lower cost for non-production/slower tasks), and Scale (reserved capacity for enterprise).
- **Rate Limits:** Limits are determined by account tier (Tier 1 to Tier 5). Tier 5 accounts typically have the highest RPM (Requests Per Minute) and TPM (Tokens Per Minute) caps.
- **Tool Billing:** Web search is billed at $10.00 per 1,000 calls. Tokens retrieved from search results are not charged.
- **Context Tiers:** Standard pricing for GPT-5 models applies to context lengths under 270K tokens. Usage exceeding this may incur different rates or require specific tiers.
