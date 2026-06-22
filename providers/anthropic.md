---
provider: Anthropic
slug: anthropic
last_updated: 2026-06-22T08:17:54Z
sources:
  - https://www.anthropic.com/pricing
  - https://platform.claude.com/docs/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [platform.claude.com/docs/en/docs/about-claude/models/overview](https://platform.claude.com/docs/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-06-22T08:17:54Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Claude 5 (Frontier)

Anthropic's most advanced generation, designed for the most demanding reasoning, long-horizon agentic work, and high-autonomy tasks. These models feature "always-on" adaptive thinking.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | `anthropic.claude-fable-5` (Bedrock), `claude-fable-5` (Vertex) | text, image | text | 1,000,000 | 128,000 | — | Stable |
| `claude-mythos-5` | `claude-mythos-preview` (Successor) | text, image | text | 1,000,000 | 128,000 | — | Preview |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | Multilingual | adaptive thinking, vision, multilingual, function calling, structured outputs, streaming, system instructions, caching, batch | — | see Notes | $10.00 / $50.00 |
| `claude-mythos-5` | Multilingual | adaptive thinking, vision, multilingual, function calling, structured outputs, streaming, system instructions, caching, batch | — | see Notes | $10.00 / $50.00 |

### Claude 4 (Latest)

The current flagship generation balancing intelligence, speed, and cost. This generation introduced extended thinking and significantly larger context windows.

| Model ID | Aliases / snapshots | Inputs | Outputs | Context window | Max output | Knowledge cutoff | Release stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | `anthropic.claude-opus-4-8` (Bedrock), `claude-opus-4-8` (Vertex) | text, image | text | 1,000,000 | 128,000 (300k Batch) | Jan 2026 | Stable |
| `claude-sonnet-4-6` | `anthropic.claude-sonnet-4-6` (Bedrock), `claude-sonnet-4-6` (Vertex) | text, image | text | 1,000,000 | 64,000 (300k Batch) | Aug 2025 | Stable |
| `claude-haiku-4-5-20251001` | `claude-haiku-4-5`, `anthropic.claude-haiku-4-5-20251001-v1:0`, `claude-haiku-4-5@20251001` | text, image | text | 200,000 | 64,000 | Feb 2025 | Stable |

| Model ID | Languages | Capabilities | Latency tier / SLA | Rate limits | Pricing (Input / Output per MTok) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-opus-4-8` | Multilingual | adaptive thinking, vision, multilingual, function calling, structured outputs, streaming, system instructions, caching, batch, priority tier | Moderate | see Notes | $5.00 / $25.00 |
| `claude-sonnet-4-6` | Multilingual | extended thinking, adaptive thinking, vision, multilingual, function calling, structured outputs, streaming, system instructions, caching, batch, priority tier | Fast | see Notes | $3.00 / $15.00 |
| `claude-haiku-4-5-20251001` | Multilingual | extended thinking, vision, multilingual, function calling, structured outputs, streaming, system instructions, caching, batch, priority tier | Fastest | see Notes | $1.00 / $5.00 |

### Specialized & Preview

Models designed for specific research or defensive workflows.

| Model ID | Description | Pricing |
| :--- | :--- | :--- |
| `claude-mythos-preview` | Research preview model for defensive cybersecurity workflows (Project Glasswing). Invitation-only. | $10.00 / $50.00 per MTok |

## Notes

*   **Batch API**: All models support the Message Batches API with a 50% discount on standard per-token rates.
*   **Prompt Caching**: Supports prefix caching for repeated context (e.g., long system prompts or documents). Caching is billed with a surcharge for "Cache Writes" and a significant discount for "Cache Reads" (typically 90% off base input rates). Cache TTL is 5 minutes, refreshed on each hit.
*   **Max Output Limits**: Synchronous Messages API limits range from 64k to 128k tokens. Claude Opus 4.8 and Sonnet 4.6 support up to 300k output tokens in the Batch API by using the `output-300k-2026-03-24` beta header.
*   **Thinking Modes**: `adaptive thinking` is always enabled for Claude 5 and Opus 4.8. `extended thinking` is an optional parameter for Sonnet 4.6 and Haiku 4.5 to improve reasoning performance on complex tasks.
*   **Effort Parameter**: Claude Opus 4.8 defaults to `high` effort for reasoning. This can be adjusted via the `effort` parameter in the API to balance latency and quality.
*   **Rate Limit Tiers**: Anthropic uses a 5-tier system based on monthly spend. Tier 1 starts at 50 RPM / 40k TPM, scaling up to Tier 5 at 10,000 RPM / 1M TPM. Limits are enforced per model family.
*   **Data Residency**: Claude Sonnet 4.5 and later support Global, Regional (guaranteed geographic routing), and Multi-region endpoints on AWS Bedrock and Google Vertex AI.
*   **Deprecation Policy**: Anthropic typically provides a 6-month notice before retiring a model version. Legacy models (Claude 3.5 and earlier) are subject to the deprecation schedule published in the official docs.
*   **Microsoft Foundry**: Claude Opus 4.8 is available on Microsoft Foundry with a reduced context window of 200,000 tokens.
