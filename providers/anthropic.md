---
provider: Anthropic
slug: anthropic
last_updated: 2026-05-19T11:37:42Z
sources:
  - https://www.anthropic.com/pricing
  - https://platform.claude.com/docs/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [platform.claude.com/docs/en/docs/about-claude/models/overview](https://platform.claude.com/docs/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-05-19T11:37:42Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Claude 4
The Claude 4 generation introduces "Adaptive Thinking" and "Extended Thinking" capabilities, alongside a significant increase in context windows (up to 1M tokens) and output limits.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-7` | `claude-opus-4-7`, `anthropic.claude-opus-4-7` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 131,072 (300k Batch) | Jan 2026 | Stable | `adaptive thinking`, `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch`, `multilingual` |
| `claude-sonnet-4-6` | `claude-sonnet-4-6`, `anthropic.claude-sonnet-4-6` (Bedrock) | `text`, `image` | `text` | 1,000,000 | 65,536 (300k Batch) | Aug 2025 | Stable | `extended thinking`, `adaptive thinking`, `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch`, `multilingual` |
| `claude-haiku-4-5-20251001` | `claude-haiku-4-5`, `anthropic.claude-haiku-4-5-20251001-v1:0` | `text`, `image` | `text` | 200,000 | 65,536 | Feb 2025 | Stable | `extended thinking`, `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch`, `multilingual` |
| `claude-opus-4-6` | `claude-opus-4-6` | `text`, `image` | `text` | 1,000,000 | 131,072 (300k Batch) | — | Stable | `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch` |
| `claude-sonnet-4-5` | `claude-sonnet-4-5` | `text`, `image` | `text` | 200,000 | 8,192 | — | Stable | `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch` |
| `claude-opus-4-5` | `claude-opus-4-5` | `text`, `image` | `text` | 200,000 | 4,096 | — | Stable | `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch` |
| `claude-opus-4-1` | `claude-opus-4-1` | `text`, `image` | `text` | 200,000 | 4,096 | — | Stable | `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch` |
| `claude-sonnet-4` | `claude-sonnet-4` | `text`, `image` | `text` | 200,000 | 4,096 | — | Stable | `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch` |
| `claude-opus-4` | `claude-opus-4` | `text`, `image` | `text` | 200,000 | 4,096 | — | Stable | `vision`, `function calling`, `structured outputs`, `streaming`, `prompt caching`, `batch` |

**Claude 4 Pricing & Latency**

| Model ID | Input $/MTok | Cache Write $/MTok | Cache Read $/MTok | Output $/MTok | Latency Tier |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-7` | 5.00 | 6.25 | 0.50 | 25.00 | Moderate |
| `claude-sonnet-4-6` | 3.00 | 3.75 | 0.30 | 15.00 | Fast |
| `claude-haiku-4-5-20251001` | 1.00 | 1.25 | 0.10 | 5.00 | Fastest |
| `claude-opus-4-6` | 5.00 | 6.25 | 0.50 | 25.00 | Moderate |
| `claude-sonnet-4-5` | 3.00 | 3.75 | 0.30 | 15.00 | Fast |
| `claude-opus-4-5` | 5.00 | 6.25 | 0.50 | 25.00 | Moderate |
| `claude-opus-4-1` | 15.00 | 18.75 | 1.50 | 75.00 | Moderate |
| `claude-sonnet-4` | 3.00 | 3.75 | 0.30 | 15.00 | Fast |
| `claude-opus-4` | 15.00 | 18.75 | 1.50 | 75.00 | Moderate |

### Claude 3.5
Claude 3.5 models introduced "Computer Use" and improved vision performance over the Claude 3 generation.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | `claude-3-5-sonnet-latest` | `text`, `image` | `text` | 200,000 | 8,192 | Apr 2024 | Stable | `vision`, `function calling`, `computer use`, `prompt caching`, `batch`, `multilingual` |
| `claude-3-5-haiku-20241022` | `claude-3-5-haiku-latest` | `text` | `text` | 200,000 | 8,192 | July 2024 | Stable | `function calling`, `prompt caching`, `batch`, `multilingual`, Not: `vision` |

**Claude 3.5 Pricing & Latency**

| Model ID | Input $/MTok | Cache Write $/MTok | Cache Read $/MTok | Output $/MTok | Latency Tier |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-5-sonnet-20241022` | 3.00 | 3.75 | 0.30 | 15.00 | Fast |
| `claude-3-5-haiku-20241022` | 0.25 | 0.30 | 0.03 | 1.25 | Fastest |

### Claude 3
The first generation to support native vision and tool use across all model sizes.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage | Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-3-opus-20240229` | `claude-3-opus-latest` | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable | `vision`, `function calling`, `streaming`, `multilingual` |
| `claude-3-sonnet-20240229` | — | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable | `vision`, `function calling`, `streaming`, `multilingual` |
| `claude-3-haiku-20240307` | — | `text`, `image` | `text` | 200,000 | 4,096 | Aug 2023 | Stable | `vision`, `function calling`, `streaming`, `multilingual` |

**Claude 3 Pricing & Latency**

| Model ID | Input $/MTok | Output $/MTok | Latency Tier |
| :--- | :--- | :--- | :--- |
| `claude-3-opus-20240229` | 15.00 | 75.00 | Moderate |
| `claude-3-sonnet-20240229` | 3.00 | 15.00 | Fast |
| `claude-3-haiku-20240307` | 0.25 | 1.25 | Fastest |

### Specialized & Research

| Model ID | Description | Inputs | Outputs | Context Window | Release Stage | Pricing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-mythos-preview` | Defensive cybersecurity research model (Project Glasswing). | `text`, `image`, `code` | `text` | — | Experimental | Invitation-only |

### Legacy Models

| Model ID | Inputs | Outputs | Context Window | Max Output | Release Stage | Pricing (In/Out $/MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-2.1` | `text` | `text` | 200,000 | 4,096 | Deprecated | 8.00 / 24.00 |
| `claude-2.0` | `text` | `text` | 100,000 | 4,096 | Deprecated | 8.00 / 24.00 |
| `claude-instant-1.2` | `text` | `text` | 100,000 | 4,096 | Deprecated | 0.80 / 2.40 |

## Notes

*   **Batch Processing**: All stable models support the Message Batches API, offering a 50% discount on standard token rates for asynchronous processing (24-hour turnaround).
*   **Prompt Caching**: Supported on Claude 4 and Claude 3.5 models. Cache Write tokens are billed at ~1.25x the standard input rate, and Cache Read tokens are billed at ~0.1x. The default TTL is 5 minutes, with extended TTL options available for Enterprise plans.
*   **Output Limits**: Standard synchronous output is capped at 64k-128k tokens for Claude 4 models. Using the `output-300k-2026-03-24` beta header with the Batch API allows for up to 300,000 output tokens on Opus 4.7, Opus 4.6, and Sonnet 4.6.
*   **Thinking Capabilities**: 
    *   **Adaptive Thinking**: Automatically adjusts reasoning depth based on task complexity (Opus 4.7, Sonnet 4.6).
    *   **Extended Thinking**: Allows the model to "think" for a longer period before responding, useful for complex math and coding (Sonnet 4.6, Haiku 4.5).
*   **Regional Pricing**: US-only inference is available for workloads requiring data residency in the United States at a 1.1x multiplier on standard input/output pricing.
*   **Rate Limits**: Limits are determined by organization tier (Tier 1–5). Tier 5 typically allows up to 10,000 RPM and 1,000,000 TPM. Specific limits per model can be queried via the `/v1/models` endpoint.
*   **Managed Agents**: Anthropic offers a Managed Agents API at $0.08 per session-hour for active runtime, in addition to standard model token rates.
*   **Web Search**: Available as a tool for Claude models at $10.00 per 1,000 searches.
*   **Code Execution**: Python code execution in a sandboxed environment is available. Organizations receive 50 free hours daily; additional usage is billed at $0.05 per hour per container.
