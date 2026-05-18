---
provider: xAI
slug: xai
last_updated: 2026-05-18T17:31:04Z
sources:
  - https://docs.x.ai/docs/models
  - https://x.ai/api
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models), [x.ai/api](https://x.ai/api)  ·  **Updated:** `2026-05-18T17:31:04Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat
| Model | Context Window | Input Price | Output Price | Capabilities |
| --- | --- | --- | --- | --- |
| `grok-4.3` | 1,000,000 tokens | $1.25 / 1M tokens | $2.50 / 1M tokens | tool calling |

### Voice
| Service | Price | Unit |
| --- | --- | --- |
| Agent | $3.00 | per hour |
| Text-to-Speech (TTS) | $15.00 | per 1M characters |
| Speech-to-Text (STT) | $0.10 | per hour |

### Image & Video
| Service | Quality | Price | Unit |
| --- | --- | --- | --- |
| Image Generation | 1K / 2K | $0.02 | per image |
| Video Generation | 480p / 720p | $0.05 | per second |

## Notes
- Several older models were retired on May 15, 2026, including `grok-4-1-fast`, `grok-4-fast`, `grok-4`, `grok-code-fast-1`, and `grok-imagine-image-pro`. Requests to these models will be redirected to `grok-4.3`.
- The knowledge cut-off date for Grok 3 and Grok 4 models is November, 2024.
- Models can be accessed via aliases. For example, `<modelname>` points to the latest stable version, while `<modelname>-latest` points to the newest version.
- Image inputs support `jpg/jpeg` or `png` file types with a maximum size of 20MiB per image.
- Chat models do not have a required role order for `system`, `user`, or `assistant` messages.
- To access real-time data, server-side search tools like Web Search or X Search must be enabled.
