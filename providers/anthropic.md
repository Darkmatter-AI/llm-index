---
provider: Anthropic
slug: anthropic
last_updated: 2026-08-10T07:49:39Z
sources:
  - https://www.anthropic.com/pricing
  - https://platform.claude.com/docs/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [platform.claude.com/docs/en/docs/about-claude/models/overview](https://platform.claude.com/docs/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-08-10T07:49:39Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Latest Generation (Claude 5 & 4.5)

The latest generation of Claude models features significantly expanded context windows (up to 1M tokens), increased output limits, and native "thinking" capabilities for complex reasoning and agentic tasks.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities | Latency Tier |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | `anthropic.claude-fable-5` (Bedrock), `claude-fable-5` (Vertex) | text, image | text | 1,000,000 | 128,000 (300,000 via Batch) | Jan 2026 | Stable | adaptive thinking, vision, tool use, prompt caching, batch, multilingual, computer use | Slower |
| `claude-opus-5` | `anthropic.claude-opus-5` (Bedrock), `claude-opus-5` (Vertex) | text, image | text | 1,000,000 | 128,000 (300,000 via Batch) | May 2026 | Stable | adaptive thinking, vision, tool use, prompt caching, batch, multilingual, computer use | Moderate |
| `claude-sonnet-5` | `anthropic.claude-sonnet-5` (Bedrock), `claude-sonnet-5` (Vertex) | text, image | text | 1,000,000 | 128,000 (300,000 via Batch) | Jan 2026 | Stable | adaptive thinking, vision, tool use, prompt caching, batch, multilingual, computer use | Fast |
| `claude-haiku-4-5-20251001` | `claude-haiku-4-5`, `anthropic.claude-haiku-4-5-20251001-v1:0` (Bedrock), `claude-haiku-4-5@20251001` (Vertex) | text, image | text | 200,000 | 64,000 | Feb 2025 | Stable | extended thinking, vision, tool use, prompt caching, batch, multilingual | Fastest |

#### Pricing (Latest)

| Model ID | Input ($/MTok) | Cached Input (Write $/MTok) | Cached Input (Read $/MTok) | Output ($/MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | $10.00 | $12.50 | $1.00 | $50.00 |
| `claude-opus-5` | $5.00 | $6.25 | $0.50 | $25.00 |
| `claude-sonnet-5` | $3.00* | $3.75 | $0.30 | $15.00* |
| `claude-haiku-4-5-20251001` | $1.00 | $1.25 | $0.10 | $5.00 |

*\*Introductory pricing of $2.00 / $10.00 per MTok applies to Claude Sonnet 5 through August 31, 2026.*

### Previous Generation (Claude 4.x)

The Claude 4 generation introduced the dateless model ID format and expanded support for global and regional endpoints on cloud providers.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities | Latency Tier |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | — | text, image | text | 200,000 | 128,000 (300,000 via Batch) | — | Stable | vision, tool use, prompt caching, batch, computer use | Moderate |
| `claude-opus-4-7` | — | text, image | text | 200,000 | 128,000 (300,000 via Batch) | — | Stable | vision, tool use, prompt caching, batch, computer use | Moderate |
| `claude-opus-4-6` | — | text, image | text | 200,000 | 128,000 (300,000 via Batch) | — | Stable | vision, tool use, prompt caching, batch, computer use | Moderate |
| `claude-sonnet-4-6` | — | text, image | text | 200,000 | 128,000 (300,000 via Batch) | — | Stable | vision, tool use, prompt caching, batch, computer use | Fast |
| `claude-sonnet-4-5` | — | text, image | text | 200,000 | 8,192 | — | Stable | vision, tool use, prompt caching, batch, computer use | Fast |

#### Pricing (Claude 4.x)

| Model ID | Input ($/MTok) | Cached Input (Write $/MTok) | Cached Input (Read $/MTok) | Output ($/MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4.x` | $5.00 | $6.25 | $0.50 | $25.00 |
| `claude-sonnet-4.x` | $3.00 | $3.75 | $0.30 | $15.00 |

### Legacy Generation (Claude 3.5 & 3)

These models established the foundation for Claude's vision and tool-use capabilities.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | `claude-3-5-sonnet-latest` | text, image | text | 200,000 | 8,192 | Apr 2024 | Stable | vision, tool use, prompt caching, batch, computer use |
| `claude-3-5-haiku-20241022` | `claude-3-5-haiku-latest` | text | text | 200,000 | 8,192 | Jul 2024 | Stable | tool use, prompt caching, batch |
| `claude-3-opus-20240229` | `claude-3-opus-latest` | text, image | text | 200,000 | 4,096 | Aug 2023 | Stable | vision, tool use, prompt caching, batch |
| `claude-3-sonnet-20240229` | — | text, image | text | 200,000 | 4,096 | Aug 2023 | Stable | vision, tool use, prompt caching, batch |
| `claude-3-haiku-20240307` | — | text, image | text | 200,000 | 4,096 | Aug 2023 | Stable | vision, tool use, prompt caching, batch |

#### Pricing (Legacy)

| Model ID | Input ($/MTok) | Cached Input (Write $/MTok) | Cached Input (Read $/MTok) | Output ($/MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet` | $3.00 | $3.75 | $0.30 | $15.00 |
| `claude-3-5-haiku` | $0.80 | $1.00 | $0.08 | $4.00 |
| `claude-3-opus` | $15.00 | $18.75 | $1.50 | $75.00 |
| `claude-3-sonnet` | $3.00 | $3.75 | $0.30 | $15.00 |
| `claude-3-haiku` | $0.25 | $0.3125 | $0.03 | $1.25 |

### Specialized

| Model ID | Description | Inputs | Outputs | Pricing |
| :--- | :--- | :--- | :--- | :--- |
| `claude-mythos-5` | Defensive cybersecurity model (Project Glasswing). Invitation-only. | text, image | text | $10.00 Input / $50.00 Output |
| `claude-mythos-preview` | Early access snapshot for Project Glasswing. | text, image | text | $10.00 Input / $50.00 Output |

### Deprecated

| Model ID | Retirement Date | Replacement |
| :--- | :--- | :--- |
| `claude-2.1` | — | `claude-3-5-sonnet` |
| `claude-2.0` | — | `claude-3-5-sonnet` |
| `claude-instant-1.2` | — | `claude-3-haiku` |

## Notes

- **Batch API:** Offers a 50% discount on all standard pricing. Supports up to 300,000 output tokens for Claude 5 and 4.6+ models using the `output-300k-2026-03-24` beta header.
- **Prompt Caching:** Minimum cacheable prompt length is 1,024 tokens (Claude 3 family) or 2,048 tokens (Claude 4/5 family). Cache TTL is 5 minutes, refreshed on every hit.
- **Thinking Modes:** 
    - **Adaptive Thinking:** Automatically adjusts reasoning depth based on task complexity (Fable 5, Opus 5, Sonnet 5).
    - **Extended Thinking:** Can be explicitly enabled via `thinking.type: "enabled"` for deep reasoning (Haiku 4.5).
- **Computer Use:** Supported on Claude 3.5 Sonnet and all Claude 4/5 models. Requires specific tool-calling schema for screen interaction.
- **Rate Limits:** Based on Tier (1–5). Tier 1 starts at 50 RPM / 40,000 TPM. Tier 5 scales to 10,000 RPM / 5,000,000 TPM. Limits are model-specific; check the Console for exact per-model quotas.
- **Data Residency:** Available via AWS Bedrock (Regional/Global endpoints) and Google Cloud Vertex AI (Regional/Multi-region/Global endpoints).
- **Model Training:** Anthropic does not train on customer data submitted via the API by default. Opt-out is available for all tiers.
