---
provider: Anthropic
slug: anthropic
last_updated: 2026-08-03T09:55:07Z
sources:
  - https://www.anthropic.com/pricing
  - https://platform.claude.com/docs/en/docs/about-claude/models/overview
---

[← Home](../) · **Anthropic** · [OpenAI](openai.md) · [Google](google.md) · [xAI](xai.md) · [DeepSeek](deepseek.md) · [Mistral](mistral.md)

# Anthropic (Claude)

**Sources:** [www.anthropic.com/pricing](https://www.anthropic.com/pricing), [platform.claude.com/docs/en/docs/about-claude/models/overview](https://platform.claude.com/docs/en/docs/about-claude/models/overview)  ·  **Updated:** `2026-08-03T09:55:07Z`

> Using Claude Code? [Install the llm-index skill](https://github.com/Darkmatter-AI/llm-index/tree/main/skill) so your agent reads this automatically instead of guessing from training data.

## Models

### Chat & Reasoning

Anthropic's primary model line, ranging from the high-intelligence Fable and Opus models to the speed-optimized Haiku models. All current models support vision and multilingual processing.

| Model ID | Aliases / Snapshots | Inputs | Outputs | Context Window | Max Output | Knowledge Cutoff | Release Stage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | `claude-fable-5`, `anthropic.claude-fable-5` (Bedrock) | text, image | text | 1,000,000 | 128,000 (300k via beta) | Jan 2026 | Stable |
| `claude-opus-5` | `claude-opus-5`, `anthropic.claude-opus-5` (Bedrock) | text, image | text | 1,000,000 | 128,000 (300k via beta) | May 2026 | Stable |
| `claude-sonnet-5` | `claude-sonnet-5`, `anthropic.claude-sonnet-5` (Bedrock) | text, image | text | 1,000,000 | 128,000 (300k via beta) | Jan 2026 | Stable |
| `claude-haiku-4-5-20251001` | `claude-haiku-4-5`, `anthropic.claude-haiku-4-5-20251001-v1:0` (Bedrock), `claude-haiku-4-5@20251001` (Vertex) | text, image | text | 200,000 | 64,000 | Feb 2025 | Stable |
| `claude-opus-4-8` | `claude-opus-4-8` | text, image | text | — | 128,000 (300k via beta) | — | Stable |
| `claude-opus-4-7` | `claude-opus-4-7` | text, image | text | — | 128,000 (300k via beta) | — | Stable |
| `claude-opus-4-6` | `claude-opus-4-6` | text, image | text | — | 128,000 (300k via beta) | — | Stable |
| `claude-sonnet-4-6` | `claude-sonnet-4-6` | text, image | text | — | 128,000 (300k via beta) | — | Stable |
| `claude-3-5-sonnet-20241022` | `claude-3-5-sonnet-latest`, `anthropic.claude-3-5-sonnet-20241022-v2:0` (Bedrock) | text, image | text | 200,000 | 8,192 | Oct 2023 | Stable |
| `claude-3-5-sonnet-20240620` | `anthropic.claude-3-5-sonnet-20240620-v1:0` (Bedrock) | text, image | text | 200,000 | 8,192 | Apr 2024 | Stable |
| `claude-3-5-haiku-20241022` | `claude-3-5-haiku-latest`, `anthropic.claude-3-5-haiku-20241022-v1:0` (Bedrock) | text, image | text | 200,000 | 8,192 | July 2024 | Stable |
| `claude-3-opus-20240229` | `claude-3-opus-latest`, `anthropic.claude-3-opus-20240229-v1:0` (Bedrock) | text, image | text | 200,000 | 4,096 | Aug 2023 | Stable |
| `claude-3-sonnet-20240229` | `anthropic.claude-3-sonnet-20240229-v1:0` (Bedrock) | text, image | text | 200,000 | 4,096 | Aug 2023 | Stable |
| `claude-3-haiku-20240307` | `anthropic.claude-3-haiku-20240307-v1:0` (Bedrock) | text, image | text | 200,000 | 4,096 | Aug 2023 | Stable |

#### Capabilities & Pricing

| Model ID | Languages | Capabilities | Latency Tier | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `claude-fable-5` | 95+ | adaptive thinking, function calling, structured outputs, streaming, prompt caching, batch, vision, multilingual | Slower | Input: $10.00<br>Cache Write: $12.50<br>Cache Read: $1.00<br>Output: $50.00 |
| `claude-opus-5` | 95+ | adaptive thinking, function calling, structured outputs, streaming, prompt caching, batch, vision, multilingual | Moderate | Input: $5.00<br>Cache Write: $6.25<br>Cache Read: $0.50<br>Output: $25.00 |
| `claude-sonnet-5` | 95+ | adaptive thinking, function calling, structured outputs, streaming, prompt caching, batch, vision, multilingual | Fast | Input: $3.00*<br>Cache Write: $3.75<br>Cache Read: $0.30<br>Output: $15.00* |
| `claude-haiku-4-5` | 95+ | extended thinking, function calling, structured outputs, streaming, prompt caching, batch, vision, multilingual | Fastest | Input: $1.00<br>Cache Write: $1.25<br>Cache Read: $0.10<br>Output: $5.00 |
| `claude-3-5-sonnet` | 95+ | computer use, function calling, structured outputs, streaming, prompt caching, batch, vision, multilingual | Fast | Input: $3.00<br>Cache Write: $3.75<br>Cache Read: $0.30<br>Output: $15.00 |
| `claude-3-5-haiku` | 95+ | function calling, structured outputs, streaming, prompt caching, batch, vision, multilingual | Fastest | Input: $1.00<br>Cache Write: $1.25<br>Cache Read: $0.10<br>Output: $5.00 |
| `claude-3-opus` | 95+ | function calling, streaming, prompt caching, batch, vision, multilingual | Moderate | Input: $15.00<br>Cache Write: $18.75<br>Cache Read: $1.50<br>Output: $75.00 |
| `claude-3-sonnet` | 95+ | function calling, streaming, vision, multilingual | Fast | Input: $3.00<br>Output: $15.00 |
| `claude-3-haiku` | 95+ | function calling, streaming, prompt caching, batch, vision, multilingual | Fastest | Input: $0.25<br>Cache Write: $0.30<br>Cache Read: $0.03<br>Output: $1.25 |

*\*Introductory pricing of $2.00 (Input) / $10.00 (Output) per MTok applies to Claude Sonnet 5 through August 31, 2026.*

### Specialized

Models designed for specific high-security or defensive workflows.

| Model ID | Description | Inputs | Outputs | Pricing (per MTok) | Release Stage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `claude-mythos-5` | Defensive cybersecurity workflows (Project Glasswing) | text, image | text | Input: $10.00<br>Output: $50.00 | Limited (Invitation-only) |
| `claude-mythos-preview` | Preview version for cybersecurity research | text, image | text | Input: $10.00<br>Output: $50.00 | Experimental |

### Deprecated

Models that are no longer recommended for new projects and have announced retirement dates.

| Model ID | Retirement Date | Inputs | Context Window | Pricing (per MTok) |
| :--- | :--- | :--- | :--- | :--- |
| `claude-2.1` | — | text | 200,000 | Input: $8.00<br>Output: $24.00 |
| `claude-2.0` | — | text | 100,000 | Input: $8.00<br>Output: $24.00 |
| `claude-instant-1.2` | — | text | 100,000 | Input: $0.80<br>Output: $2.40 |

## Notes

- **Prompt Caching**: Anthropic offers prompt caching with a 5-minute (300-second) TTL. Cache writes are billed at 1.25x the base input rate, and cache reads are billed at 0.1x the base input rate.
- **Batch API**: The Message Batches API provides a 50% discount on standard pricing for asynchronous processing (up to 24-hour turnaround).
- **Extended Output**: Claude 5 and Claude 4 models support up to 300,000 output tokens in batch mode using the `output-300k-2026-03-24` beta header.
- **Thinking Modes**: "Adaptive thinking" is always enabled on Fable 5, Opus 5, and Sonnet 5 to optimize reasoning effort. "Extended thinking" on Haiku 4.5 is controlled via the `thinking.type: "enabled"` parameter.
- **Rate Limit Tiers**:
    - **Tier 1**: 5 RPM / 20,000 TPM / 50,000 RPD
    - **Tier 2**: 50 RPM / 100,000 TPM / 500,000 RPD
    - **Tier 3**: 100 RPM / 200,000 TPM / 1,000,000 RPD
    - **Tier 4**: 1,000 RPM / 400,000 TPM / 5,000,000 RPD
    - **Tier 5**: 10,000 RPM / 5,000,000 TPM / 10,000,000 RPD
- **Data Residency**: Anthropic offers regional endpoints on AWS Bedrock and Google Cloud Vertex AI for guaranteed data routing through specific geographic regions (e.g., US, EU).
- **Computer Use**: This capability is currently exclusive to the Claude 3.5 Sonnet model family and allows the model to interact with virtual desktop environments.
