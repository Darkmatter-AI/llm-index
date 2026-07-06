---
provider: Anthropic
slug: anthropic
last_updated: 2026-07-06T07:45:11Z
sources:
  - https://www.anthropic.com/pricing
  - https://platform.claude.com/docs/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [platform.claude.com/docs/en/docs/about-claude/models/overview](https://platform.claude.com/docs/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-07-06T07:45:11Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Claude 5 Generation
The latest generation of Claude models, featuring next-generation intelligence, adaptive thinking, and massive context windows.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | `anthropic.claude-fable-5` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 128,000 | Jan 2026 | Stable |
| `claude-mythos-5` | `claude-mythos-preview` | `text`, `image` | `text` | 1,000,000 | 128,000 | Jan 2026 | Preview |
| `claude-sonnet-5` | `anthropic.claude-sonnet-5` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 128,000 | Jan 2026 | Stable |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | Multilingual | `vision`, `tool use`, `adaptive thinking`, `prompt caching`, `batch`, `streaming` | Slower | see Notes | $10.00 / $50.00 |
| `claude-mythos-5` | Multilingual | `vision`, `tool use`, `adaptive thinking`, `prompt caching`, `batch`, `streaming` | Slower | see Notes | $10.00 / $50.00 |
| `claude-sonnet-5` | Multilingual | `vision`, `tool use`, `computer use`, `adaptive thinking`, `prompt caching`, `batch`, `streaming`, `extended output` (300k beta) | Fast | see Notes | $3.00 / $15.00 ($2.00 / $10.00 intro) |

### Claude 4 Generation
High-performance models optimized for agentic coding, enterprise workflows, and reasoning.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | `anthropic.claude-opus-4-8` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 128,000 | Jan 2026 | Stable |
| `claude-haiku-4-5-20251001` | `claude-haiku-4-5` | `text`, `image` | `text` | 200,000 | 64,000 | Feb 2025 | Stable |
| `claude-opus-4-7` | — | `text`, `image` | `text` | 1,000,000 | 128,000 | — | Stable |
| `claude-sonnet-4-6` | — | `text`, `image` | `text` | 1,000,000 | 128,000 | — | Stable |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | Multilingual | `vision`, `tool use`, `adaptive thinking`, `prompt caching`, `batch`, `streaming`, `extended output` (300k beta) | Moderate | see Notes | $5.00 / $25.00 |
| `claude-haiku-4-5-20251001` | Multilingual | `vision`, `tool use`, `extended thinking`, `prompt caching`, `batch`, `streaming` | Fastest | see Notes | $1.00 / $5.00 |
| `claude-opus-4-7` | Multilingual | `vision`, `tool use`, `prompt caching`, `batch`, `streaming`, `extended output` (300k beta) | Moderate | see Notes | $5.00 / $25.00 |
| `claude-sonnet-4-6` | Multilingual | `vision`, `tool use`, `computer use`, `prompt caching`, `batch`, `streaming`, `extended output` (300k beta) | Fast | see Notes | $3.00 / $15.00 |

### Claude 3.5 & 3 Generation
Legacy frontier models providing a balance of speed and capability for established integrations.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | `claude-3-5-sonnet-latest` | `text`, `image` | `text` | 200,000 | 8,192 | Oct 2023 | Stable |
| `claude-3-5-haiku-20241022` | `claude-3-5-haiku-latest` | `text` | `text` | 200,000 | 8,192 | Jul 2024 | Stable |
| `claude-3-opus-20240229` | `claude-3-opus-latest` | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable |
| `claude-3-sonnet-20240229` | — | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable |
| `claude-3-haiku-20240307` | — | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | Multilingual | `vision`, `tool use`, `computer use`, `prompt caching`, `batch`, `streaming` | Fast | see Notes | $3.00 / $15.00 |
| `claude-3-5-haiku-20241022` | Multilingual | `tool use`, `prompt caching`, `batch`, `streaming` | Fastest | see Notes | $0.80 / $4.00 |
| `claude-3-opus-20240229` | Multilingual | `vision`, `tool use`, `prompt caching`, `batch`, `streaming` | Moderate | see Notes | $15.00 / $75.00 |
| `claude-3-sonnet-20240229` | Multilingual | `vision`, `tool use`, `prompt caching`, `batch`, `streaming` | Fast | see Notes | $3.00 / $15.00 |
| `claude-3-haiku-20240307` | Multilingual | `vision`, `tool use`, `prompt caching`, `batch`, `streaming` | Fastest | see Notes | $0.25 / $1.25 |

### Specialized & Deprecated
Older models maintained for backward compatibility or specific legacy use cases.

| Model ID | Description | Context window | Pricing (Input / Output per MTok) | Release stage |
| :--- | :--- | :--- | :--- | :--- |
| `claude-2.1` | Legacy model | 200,000 | $8.00 / $24.00 | Deprecated |
| `claude-2.0` | Legacy model | 100,000 | $8.00 / $24.00 | Deprecated |
| `claude-instant-1.2` | Legacy fast model | 100,000 | $0.80 / $2.40 | Deprecated |

## Notes

- **Batch API**: All models support the Message Batches API, offering a 50% discount on standard pricing for asynchronous processing within 24 hours.
- **Prompt Caching**: Supported on all Claude 3, 3.5, 4, and 5 models. Cache writes cost +25% of the base input price; cache reads cost 10% of the base input price (90% discount). Minimum cacheable length is 1,024 tokens (Claude 3.5/4/5) or 8,192 tokens (Claude 3). TTL is 5 minutes.
- **Extended Output**: Claude Opus 4.8, 4.7, 4.6, Sonnet 5, and Sonnet 4.6 support up to 300,000 output tokens via the `anthropic-beta: output-300k-2026-03-24` header.
- **Adaptive Thinking**: A feature in Claude 5 and Opus 4.8 that allows the model to dynamically allocate reasoning effort. On Claude Opus 4.8 and Sonnet 5, the `effort` parameter defaults to `high`.
- **Computer Use**: Specifically supported by Claude 5 Sonnet, Claude 4.6 Sonnet, and Claude 3.5 Sonnet, allowing the model to interact with GUI elements.
- **Rate Limits**: Anthropic uses a Tier-based system (Tier 1 to Tier 5). Tier 1 typically starts at 50 RPM / 50,000 TPM, while Tier 5 can reach 10,000 RPM / 5,000,000 TPM depending on the model.
- **Data Residency**: Regional endpoints are available on AWS Bedrock and Google Cloud Vertex AI for guaranteed data routing through specific geographic regions (e.g., US, EU).
- **Deprecation Policy**: Anthropic typically provides 6 months' notice before retiring a model version. Deprecated models remain accessible until their announced shutdown date.
