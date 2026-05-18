---
provider: Anthropic
slug: anthropic
last_updated: 2026-05-18T15:35:15Z
sources:
  - https://www.anthropic.com/pricing
  - https://docs.anthropic.com/en/docs/about-claude/models/overview
---

# Anthropic (Claude)

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

### Claude Opus 4.7
- **Model ID**: `claude-opus-4-7`
- **Context window**: 1M tokens
- **Max output**: 128k tokens
- **Input price**: $5 / 1M tokens
- **Output price**: $25 / 1M tokens
- **Cached input price**:
    - Write: $6.25 / 1M tokens
    - Read: $0.50 / 1M tokens
- **Capabilities**: vision, text, multilingual
- **Knowledge cutoff**: January 2026
- **Notes**: Most capable model for complex reasoning and agentic coding.

### Claude Sonnet 4.6
- **Model ID**: `claude-sonnet-4-6`
- **Context window**: 1M tokens
- **Max output**: 64k tokens
- **Input price**: $3 / 1M tokens
- **Output price**: $15 / 1M tokens
- **Cached input price**:
    - Write: $3.75 / 1M tokens
    - Read: $0.30 / 1M tokens
- **Capabilities**: vision, text, multilingual
- **Knowledge cutoff**: August 2025
- **Notes**: The best combination of speed and intelligence.

### Claude Haiku 4.5
- **Model ID**: `claude-haiku-4-5-20251001`
- **Context window**: 200k tokens
- **Max output**: 64k tokens
- **Input price**: $1 / 1M tokens
- **Output price**: $5 / 1M tokens
- **Cached input price**:
    - Write: $1.25 / 1M tokens
    - Read: $0.10 / 1M tokens
- **Capabilities**: vision, text, multilingual
- **Knowledge cutoff**: February 2025
- **Notes**: The fastest model with near-frontier intelligence.

## Notes
- Asynchronous batch processing is available at a 50% discount.
- Prompt caching is offered with separate "Write" and "Read" prices, reflecting a 5-minute TTL.
- US-only data inference is available for a 1.1x price multiplier on input and output tokens.
- A free tier is available for individuals to try Claude via the web and mobile apps.
- All Claude model IDs are pinned snapshots, not evergreen pointers.
- Anthropic maintains a model deprecation policy for older versions.
