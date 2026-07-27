---
provider: Anthropic
slug: anthropic
last_updated: 2026-07-27T10:00:03Z
sources:
  - https://www.anthropic.com/pricing
  - https://platform.claude.com/docs/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [platform.claude.com/docs/en/docs/about-claude/models/overview](https://platform.claude.com/docs/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-07-27T10:00:03Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Claude 5 Generation (Chat / Reasoning)

The Claude 5 generation introduces "Adaptive Thinking" (always-on reasoning) for flagship models and expanded 1M token context windows.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | `anthropic.claude-fable-5` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 128,000 (300k via Batch) | Jan 2026 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual, computer use, adaptive thinking |
| `claude-opus-5` | `anthropic.claude-opus-5` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 128,000 (300k via Batch) | May 2026 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual, computer use, adaptive thinking |
| `claude-sonnet-5` | `anthropic.claude-sonnet-5` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 128,000 (300k via Batch) | Jan 2026 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual, computer use, adaptive thinking |
| `claude-haiku-4-5-20251001` | `claude-haiku-4-5`, `anthropic.claude-haiku-4-5-20251001-v1:0` | `text`, `image` | `text` | 200,000 | 64,000 | Feb 2025 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual, extended thinking |

#### Claude 5 Pricing & Latency

| Model ID | Latency Tier | Input $/MTok | Cached Input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | Moderate | $10.00 | Write: $12.50 / Read: $1.00 | $50.00 |
| `claude-opus-5` | Moderate | $5.00 | Write: $6.25 / Read: $0.50 | $25.00 |
| `claude-sonnet-5` | Fast | $3.00* | Write: $3.75 / Read: $0.30 | $15.00* |
| `claude-haiku-4-5-20251001` | Fastest | $1.00 | Write: $1.25 / Read: $0.10 | $5.00 |

*\*Introductory pricing of $2.00 / $10.00 per MTok applies to Claude Sonnet 5 through August 31, 2026.*

### Claude 4 Generation (Chat / Reasoning)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | — | `text`, `image` | `text` | 200,000 | 128,000 | — | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual, computer use |
| `claude-opus-4-7` | — | `text`, `image` | `text` | 200,000 | 128,000 | — | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual |
| `claude-opus-4-6` | — | `text`, `image` | `text` | 200,000 | 128,000 | — | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual |
| `claude-sonnet-4-6` | — | `text`, `image` | `text` | 200,000 | 128,000 | — | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, multilingual, computer use |

#### Claude 4 Pricing & Latency

| Model ID | Latency Tier | Input $/MTok | Cached Input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | Moderate | $15.00 | Write: $18.75 / Read: $1.50 | $75.00 |
| `claude-opus-4-7` | Moderate | $15.00 | Write: $18.75 / Read: $1.50 | $75.00 |
| `claude-opus-4-6` | Moderate | $15.00 | Write: $18.75 / Read: $1.50 | $75.00 |
| `claude-sonnet-4-6` | Fast | $3.00 | Write: $3.75 / Read: $0.30 | $15.00 |

### Claude 3 & 3.5 Generation (Legacy)

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | `claude-3-5-sonnet-latest` | `text`, `image` | `text` | 200,000 | 8,192 | Oct 2023 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision, computer use |
| `claude-3-5-haiku-20241022` | `claude-3-5-haiku-latest` | `text` | `text` | 200,000 | 8,192 | Jul 2024 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, Not: vision |
| `claude-3-opus-20240229` | `claude-3-opus-latest` | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision |
| `claude-3-sonnet-20240229` | — | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable | function calling, structured outputs, streaming, system instructions, vision |
| `claude-3-haiku-20240307` | — | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable | function calling, structured outputs, streaming, system instructions, prompt caching, batch, vision |

#### Claude 3 & 3.5 Pricing & Latency

| Model ID | Latency Tier | Input $/MTok | Cached Input $/MTok | Output $/MTok |
| :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | Fast | $3.00 | Write: $3.75 / Read: $0.30 | $15.00 |
| `claude-3-5-haiku-20241022` | Fastest | $0.80 | Write: $1.00 / Read: $0.08 | $4.00 |
| `claude-3-opus-20240229` | Moderate | $15.00 | Write: $18.75 / Read: $1.50 | $75.00 |
| `claude-3-sonnet-20240229` | Fast | $3.00 | — | $15.00 |
| `claude-3-haiku-20240307` | Fastest | $0.25 | Write: $0.30 / Read: $0.03 | $1.25 |

### Specialized

#### Project Glasswing (Cybersecurity)

| Model ID | Description | Inputs | Outputs | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `claude-mythos-5` | Defensive cybersecurity workflows; invitation-only. | `text`, `image` | `text` | Same as `claude-fable-5` |
| `claude-mythos-preview` | Early access preview for approved customers. | `text`, `image` | `text` | Same as `claude-fable-5` |

## Notes

- **Batch API**: All models (except previews) support the Message Batches API with a 50% discount on standard pricing. Results are typically returned within 24 hours.
- **Prompt Caching**: Supported on most Claude 3, 4, and 5 models. Minimum cacheable prompt length is 1,024 tokens (Haiku) or 2,048 tokens (Sonnet/Opus/Fable). Cache TTL is 5 minutes of inactivity.
- **Rate Limits**: Tier-based limits apply to the Claude API. Tier 1 starts at 50 RPM / 40,000 TPM. Tier 5 scales to 10,000+ RPM and 5,000,000+ TPM depending on the model.
- **Extended Thinking**: Available on `claude-haiku-4-5` via the `thinking` parameter. Users can set a `budget_tokens` value to control reasoning depth.
- **Adaptive Thinking**: Enabled by default on Claude 5 flagship models (`fable`, `opus`, `sonnet`). The model automatically scales internal reasoning steps based on task complexity.
- **Max Output Beta**: Claude 4 and 5 models support up to 300,000 output tokens in the Batch API by including the `output-300k-2026-03-24` beta header.
- **Data Residency**: Regional endpoints are available on Amazon Bedrock and Google Cloud Vertex AI for guaranteed data routing within specific geographic regions (US, EU, APAC).
- **Model Training**: Anthropic does not train its generative models on customer data submitted via the API by default. Enterprise and Team plans include explicit opt-out guarantees.
