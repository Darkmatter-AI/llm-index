---
provider: OpenAI
slug: openai
last_updated: 2026-05-18T16:11:16Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [openai.com/api/pricing](https://openai.com/api/pricing/), [platform.openai.com/docs/models](https://platform.openai.com/docs/models)  ·  **Updated:** `2026-05-18T16:11:16Z`

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GPT-5.5 | `` `gpt-5.5` `` | 1M | 128K | $5.00 | $30.00 | $0.50 | vision, tools, web search, file search, computer use | Dec 2025 |
| GPT-5.4 | `` `gpt-5.4` `` | 1M | 128K | $2.50 | $15.00 | $0.25 | vision, tools, web search, file search, computer use | Aug 2025 |
| GPT-5.4 mini | `` `gpt-5.4-mini` `` | 400K | 128K | $0.75 | $4.50 | $0.075 | vision, tools, web search, file search, computer use | Aug 2025 |
| GPT-Image-2 | `` `gpt-image-2` `` | — | — | $5.00 | — | $1.25 | vision, image generation | — |
| GPT-Realtime-2 | `` `gpt-realtime-2` `` | — | — | $4.00 | $24.00 | $0.40 | vision, audio, speech | — |

## Notes

* The Batch API provides a 50% discount on inputs and outputs for asynchronous tasks that complete within 24 hours.
* Prompt caching is available at a reduced rate for repeated input tokens.
* Several models are available for fine-tuning to optimize for specific use cases.
* A "Flex processing" service tier offers lower costs for non-production tasks in exchange for slower response times.
* Data residency options are available for an additional 10% cost on standard processing rates.
* OpenAI provides documentation and migration guides for deprecated models.
