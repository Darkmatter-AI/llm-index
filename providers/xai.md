---
provider: xAI
slug: xai
last_updated: 2026-05-18T15:35:15Z
sources:
  - https://docs.x.ai/docs/models
  - https://x.ai/api
---

# xAI (Grok)

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

### Grok 4.3
- **Model ID**: grok-4.3
- **Context window**: 1 million tokens
- **Input price**: $1.25 / 1M tokens
- **Output price**: $2.50 / 1M tokens
- **Capabilities**: vision, tool use, reasoning
- **Knowledge cutoff**: November, 2024
- **Notes**: Newest flagship model.

### grok-4.20-reasoning
- **Model ID**: grok-4.20-reasoning
- **Context window**: 2M
- **Input price**: $1.25 / 1M tokens
- **Output price**: $2.50 / 1M tokens
- **Capabilities**: tool use, reasoning
- **Knowledge cutoff**: November, 2024

### grok-4.20-non-reasoning
- **Model ID**: grok-4.20-non-reasoning
- **Context window**: 2M
- **Input price**: $1.25 / 1M tokens
- **Output price**: $2.50 / 1M tokens
- **Notes**: For latency-sensitive use cases.

## Notes
- The API is compatible with OpenAI and Anthropic's SDKs.
- A Batch API is available for deferred completions.
- Prompt caching is an available feature.
- Several older models were retired on May 15, 2026.
- The knowledge cut-off date for Grok 4 is November, 2024.
- Models do not have access to real-time events unless search tools are enabled.
- Model aliases are available to automatically point to the latest stable or newest version.
