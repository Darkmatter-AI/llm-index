---
provider: OpenAI
slug: openai
last_updated: 2026-05-18T17:31:04Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [openai.com/api/pricing](https://openai.com/api/pricing/), [platform.openai.com/docs/models](https://platform.openai.com/docs/models)  ·  **Updated:** `2026-05-18T17:31:04Z`

## Models

### Frontier Models

Our frontier models are designed for complex, multi-step problems.

| Model | Input | Cached Input | Output | Context Window | Capabilities |
| --- | --- | --- | --- | --- | --- |
| `gpt-5.5` | $5.00 / MTok | $0.50 / MTok | $30.00 / MTok | 1M tokens | vision, tools, reasoning |
| `gpt-5.4` | $2.50 / MTok | $0.25 / MTok | $15.00 / MTok | 1M tokens | vision, tools, reasoning |
| `gpt-5.4-mini` | $0.75 / MTok | $0.075 / MTok | $4.50 / MTok | 400K tokens | vision, tools, reasoning |

### Multimodal

These models power applications across text, image, and audio.

| Model | Modality | Input Price | Cached Input Price | Output Price |
| --- | --- | --- | --- | --- |
| `gpt-realtime-2` | Audio | $32.00 / MTok | $0.40 / MTok | $64.00 / MTok |
| | Text | $4.00 / MTok | $0.40 / MTok | $24.00 / MTok |
| | Image | $5.00 / MTok | $0.50 / MTok | |

| Model | Price |
| --- | --- |
| `gpt-realtime-translate` | $0.034 / minute |
| `gpt-realtime-whisper` | $0.017 / minute |

### Image Generation

| Model | Modality | Input Price | Cached Input Price | Output Price |
| --- | --- | --- | --- | --- |
| `gpt-image-2` | Image | $8.00 / MTok | $2.00 / MTok | $30.00 / MTok |
| | Text | $5.00 / MTok | $1.25 / MTok | |

### Tools

Tools extend model capabilities with retrieval, execution, and external data access.

| Tool | Price |
| --- | --- |
| Web search | $10.00 / 1k calls |
| Containers | $0.03 / GB per 20-minute session |

## Notes

- The Batch API provides a 50% discount on standard input and output pricing for asynchronous tasks.
- Using cached inputs for repeated prompts results in a significant price reduction compared to standard input tokens.
- Data residency and regional processing are available for a 10% surcharge on standard processing rates.
- In addition to standard processing, OpenAI offers Priority processing for higher throughput and Flex processing for lower costs on non-production tasks.
- Enterprise offerings with SLAs, lower latency, and reserved capacity are available by contacting sales.
- For pricing purposes, images are converted into tokens, with rates varying by model.
