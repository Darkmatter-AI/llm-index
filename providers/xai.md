---
provider: xAI
slug: xai
last_updated: 2026-08-10T07:49:39Z
sources:
  - https://docs.x.ai/docs/models
---

[← Home](../) · [Anthropic](anthropic.md) · [OpenAI](openai.md) · [Google](google.md) · **xAI** · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# xAI (Grok)

**Sources:** [docs.x.ai/docs/models](https://docs.x.ai/docs/models)  ·  **Updated:** `2026-08-10T07:49:39Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat / Reasoning

Grok 4.5 is the flagship model generation, featuring a significantly expanded context window and native agentic capabilities. Grok 4.20 is a specialized variant that removes support for logprobs in favor of other performance optimizations.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Languages |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | `grok-4.5-latest`, `grok-4.5-20260201` | text, image | text | 500,000 | — | Feb 2026 | Stable | — |
| `grok-4.20` | `grok-4.20-latest` | text, image | text | — | — | — | Stable | — |

| Model ID | Capabilities | Latency Tier / SLA | Rate Limits | Pricing (USD) |
| :--- | :--- | :--- | :--- | :--- |
| `grok-4.5` | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, vision, reasoning, multi agent, context compaction, priority processing | Fastest | see Notes | Input: $2.00 / MTok<br>Output: $6.00 / MTok |
| `grok-4.20` | function calling, structured outputs, streaming, system instructions, prompt caching, batch, code execution, web search, X search, vision, reasoning, multi agent, context compaction, priority processing, Not: logprobs, Not: top_logprobs | — | see Notes | — |

### Image / Video (Imagine API)

The Imagine API provides high-speed generation and editing for visual media.

| Model ID | Inputs | Output Resolution(s) | Pricing (USD) |
| :--- | :--- | :--- | :--- |
| `grok-imagine` | text, image, image+mask | **Image:** 1K, 2K<br>**Video:** 480p, 720p, 1080p | **Image:** $0.02 / image<br>**Video:** $0.05 / second |

### Voice API

The Voice API supports real-time conversational agents, text-to-speech (TTS), and speech-to-text (STT).

| Model ID | Direction | Capabilities | Pricing (USD) |
| :--- | :--- | :--- | :--- |
| `grok-voice` | TTS, STT, Speech-to-Speech | Real-time conversations, ephemeral tokens, custom voices | **Agent:** $0.05 / min<br>**TTS:** $15.00 / MChars<br>**STT (Batch):** $0.10 / hour<br>**STT (Streaming):** $0.20 / hour |

### Deprecated

These models were officially retired on May 15, 2026.

| Model ID | Retirement Date |
| :--- | :--- |
| `grok-2` | May 15, 2026 |
| `grok-2-1212` | May 15, 2026 |
| `grok-2-mini` | May 15, 2026 |
| `grok-2-mini-1212` | May 15, 2026 |
| `grok-2-vision-1212` | May 15, 2026 |
| `grok-beta` | May 15, 2026 |
| `grok-vision-beta` | May 15, 2026 |

## Notes

- **Rate Limits:** xAI uses a 5-tier system (Tier 1 to Tier 5) based on account age and usage history. Specific RPM/TPM limits are managed via the API Console.
- **Prompt Caching:** Supported for Grok 4.5 and newer. Features "Context Compaction" to optimize long-context performance.
- **Batch API:** Offers "Deferred Completions" for non-urgent workloads.
- **Search Grounding:** Real-time data access requires enabling `Web Search` or `X Search` tools; the base models do not have real-time knowledge beyond their cutoff.
- **Vision Specs:** Maximum image size is 20MiB. Supported formats include `jpg`, `jpeg`, and `png`. There is no limit on the number of images per request.
- **Role Flexibility:** Chat models have no role order limitation; `system`, `user`, and `assistant` roles can be mixed in any sequence.
- **Regional Options:** Enterprise deployments support mTLS authentication and dedicated regional endpoints.
- **Logprobs:** Support for `logprobs` and `top_logprobs` is discontinued for models `grok-4.20` and newer.
