---
provider: OpenAI
slug: openai
last_updated: 2026-07-20T09:24:02Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · **OpenAI** · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# OpenAI (GPT)

**Sources:** [openai.com/api/pricing](https://openai.com/api/pricing/), [platform.openai.com/docs/models](https://platform.openai.com/docs/models)  ·  **Updated:** `2026-07-20T09:24:02Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Frontier

The GPT-5.6 series represents the latest generation of frontier models, featuring a unified 1.05M context window and advanced reasoning capabilities. All models in this series support multimodal inputs and "Computer Use" for direct interaction with digital interfaces.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | `gpt-5.6` | text, image, audio, video, code | text, audio, image | 1,050,000 | 128,000 | Feb 2026 | Stable | Multilingual |
| `gpt-5.6-terra` | — | text, image, audio, video, code | text, audio, image | 1,050,000 | 128,000 | Feb 2026 | Stable | Multilingual |
| `gpt-5.6-luna` | — | text, image, audio, video, code | text, audio, image | 1,050,000 | 128,000 | Feb 2026 | Stable | Multilingual |
| `gpt-5.5-instant` | — | text, image, audio, video, code | text, audio, image | 128,000 | — | — | Stable | Multilingual |

| Model ID | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input/Output per MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-5.6-sol` | function calling, web search, file search, computer use, vision, multilingual, structured outputs, streaming, prompt caching, batch | Fastest | see Notes | $5.00 / $30.00 |
| `gpt-5.6-terra` | function calling, web search, file search, computer use, vision, multilingual, streaming, prompt caching, batch | Fast | see Notes | $2.50 / $15.00 |
| `gpt-5.6-luna` | function calling, web search, file search, computer use, vision, multilingual, streaming, prompt caching, batch | Moderate | see Notes | $1.00 / $6.00 |
| `gpt-5.5-instant` | function calling, vision, multilingual, streaming, prompt caching, batch | Fastest | see Notes | — |

### Realtime

Models optimized for low-latency, streaming speech-to-speech and multimodal interactions.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `gpt-realtime-2.1` | — | text, audio | text, audio | — | — | — | Stable | reasoning, tool use, streaming |
| `gpt-realtime-2.1-mini` | — | text, audio | text, audio | — | — | — | Stable | reasoning, tool use, streaming |
| `gpt-realtime-2` | — | text, audio | text, audio | — | — | — | Stable | reasoning, tool use, streaming |
| `gpt-realtime-translate` | — | audio | audio | — | — | — | Stable | speech-to-speech translation |
| `gpt-realtime-1.5` | — | audio | audio | — | — | — | Stable | audio in, audio out |
| `gpt-realtime-mini` | — | text, audio | text, audio | — | — | — | Stable | cost-efficient realtime |

### Image

| Model ID | Inputs | Output resolution(s) | Price per image | Batch discount |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-image-2` | text, image | — | — | — |

### Audio & Transcription

| Model ID | Direction | Supported languages | Price per minute / MTok |
| :--- | :--- | :--- | :--- |
| `gpt-realtime-whisper` | STT (Streaming) | — | — |
| `gpt-4o-transcribe` | STT | — | — |
| `gpt-4o-mini-transcribe` | STT | — | — |

### Deprecated

| Model ID | Replacement | Retirement date |
| :--- | :--- | :--- |
| `gpt-4o-mini-tts` | — | — |

## Notes

- **Prompt Caching**: Automatic caching is enabled for all GPT-5.6 and GPT-5.5 models. Cached input tokens receive a 50% discount compared to standard input pricing.
- **Batch API**: Asynchronous requests via the Batch API are processed within 24 hours and receive a 50% discount on all token costs.
- **Data Residency**: OpenAI supports data residency for Enterprise customers in 10 regions: US, EU, UK, JP, CA, KR, SG, IN, AU, and UAE.
- **Rate Limits**: Limits are determined by organization usage tiers (Tier 1 through Tier 5). Higher tiers provide significantly increased RPM (Requests Per Minute) and TPM (Tokens Per Minute) caps.
- **Training Policy**: Data submitted via the API is not used to train OpenAI models by default for Business and Enterprise plans.
- **Computer Use**: The GPT-5.6 series supports "Computer Use" capabilities, allowing the model to perceive and interact with software interfaces via the API.
- **Context Management**: For ChatGPT-integrated runs, the system manages a shared context window where a portion is reserved for system instructions, memories, and internal reasoning.
