---
provider: xAI
slug: xai
last_updated: 2026-05-18T15:48:38Z
sources:
  - https://docs.x.ai/docs/models
  - https://x.ai/api
---

# xAI (Grok)

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

| Model | ID | Context | Max Out | Input $/MTok | Output $/MTok | Cached In $/MTok | Capabilities | Cutoff |
|---|---|---|---|---|---|---|---|---|
| Grok 4.3 | `grok-4.3` | 1M | — | $1.25 | $2.50 | — | tools, reasoning | Nov 2024 |
| Grok 4.20 | `grok-4.20-reasoning` | 2M | — | $1.25 | $2.50 | — | tools, reasoning | Nov 2024 |
| Grok 4.20 | `grok-4.20-non-reasoning` | 2M | — | $1.25 | $2.50 | — | — | Nov 2024 |

## Notes

*   The API is compatible with OpenAI and Anthropic SDKs, requiring only a URL and API key change to migrate.
*   Prompt caching is available as an advanced API feature.
*   Server-side tools for Web Search and X Search can be enabled to provide models with real-time information.
*   The knowledge cut-off date for Grok 3 and Grok 4 models is November, 2024.
*   A number of older models were retired on May 15, 2026, with requests being redirected to `grok-4.3`.
*   The API supports vision for interpreting images, though pricing is not listed for the chat models.
*   Batch API and deferred completions are available for advanced use cases.
