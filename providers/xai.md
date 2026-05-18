---
provider: xAI
slug: xai
last_updated: 2026-05-18T17:18:48Z
sources:
  - https://docs.x.ai/docs/models
  - https://x.ai/api
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models), [x.ai/api](https://x.ai/api)  ·  **Updated:** `2026-05-18T17:18:48Z`  ·  [JSON](../data/xai.json)

## Models

### Chat / completion

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grok 4.3 | `grok-4.3` | 1M | — | $1.25 | $2.5 | — | tools, reasoning | Nov 2024 |
| Grok 4.20 Non-Reasoning | `grok-4.20-non-reasoning` | 2M | — | $1.25 | $2.5 | — | — | Nov 2024 |

### Reasoning

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grok 4.20 Reasoning | `grok-4.20-reasoning` | 2M | — | $1.25 | $2.5 | — | tools, reasoning | Nov 2024 |

### Image generation

| Model | ID | Text In $/MTok | Image In $/MTok | Image Out | Unit | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Imagine API - Image | `imagine-api-image` | — | — | $0.02 | $/image | Turn ideas into reality with image and video generation. |

### Video generation

| Model | ID | Pricing | Notes |
| --- | --- | --- | --- |
| Imagine API - Video | `imagine-api-video` | output: $0.05/second | Turn ideas into reality with image and video generation. |

### Speech — transcription / TTS / translation

| Model | ID | Input | Output | Unit | Notes |
| --- | --- | --- | --- | --- | --- |
| Voice API | `voice-api` | — | — | $/MTok | Real-time conversations, speech-to-text, and text-to-speech. |

## Notes

- The API is compatible with OpenAI and Anthropic's SDKs, allowing for easy migration.
- Several older models are scheduled for retirement on May 15, 2026. Requests to these models will be redirected to grok-4.3 and charged accordingly.
- The knowledge cut-off date for Grok 4 models is November, 2024.
- Enterprise features include SSO, audit logging, authorization controls, and compliance with standards like SOC 2 Type 2 and GDPR.
- To incorporate real-time data, server-side search tools (Web Search / X Search) must be enabled.

