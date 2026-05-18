---
provider: Google
slug: google
last_updated: 2026-05-18T15:35:15Z
sources:
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/models
---

# Google (Gemini)

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

### Gemini 3.1 Pro
- **Model ID**: gemini-3.1-pro-preview
- **Input price**: 
    - $2.00 / 1M tokens (prompts <= 200k tokens)
    - $4.00 / 1M tokens (prompts > 200k tokens)
- **Output price**:
    - $12.00 / 1M tokens (prompts <= 200k tokens)
    - $18.00 / 1M tokens (prompts > 200k)
- **Cached input price**:
    - $0.20 / 1M tokens (prompts <= 200k tokens)
    - $0.40 / 1M tokens (prompts > 200k)
- **Capabilities**: vision, tool use, reasoning, audio
- **Notes**: Preview model.

### Gemini 3.1 Flash-Lite
- **Model ID**: gemini-3.1-flash-lite
- **Input price**: $0.25 / 1M tokens (text / image / video), $0.50 / 1M tokens (audio)
- **Output price**: $1.50 / 1M tokens
- **Cached input price**: $0.025 / 1M tokens (text / image / video), $0.05 / 1M tokens (audio)
- **Capabilities**: vision, tool use, reasoning, audio

### Gemini 2.5 Pro
- **Model ID**: gemini-2.5-pro
- **Context window**: 1M tokens
- **Input price**:
    - $1.25 / 1M tokens (prompts <= 200k tokens)
    - $2.50 / 1M tokens (prompts > 200k tokens)
- **Output price**:
    - $10.00 / 1M tokens (prompts <= 200k tokens)
    - $15.00 / 1M tokens (prompts > 200k)
- **Cached input price**:
    - $0.125 / 1M tokens (prompts <= 200k tokens)
    - $0.25 / 1M tokens (prompts > 200k)
- **Capabilities**: vision, tool use, reasoning, audio, coding

### Gemini 2.5 Flash
- **Model ID**: gemini-2.5-flash
- **Context window**: 1M tokens
- **Input price**: $0.30 / 1M tokens (text / image / video), $1.00 / 1M tokens (audio)
- **Output price**: $2.50 / 1M tokens
- **Cached input price**: $0.03 / 1M tokens (text / image / video), $0.10 / 1M tokens (audio)
- **Capabilities**: vision, tool use, reasoning, audio

### Gemini 2.5 Flash-Lite
- **Model ID**: gemini-2.5-flash-lite
- **Input price**: $0.10 / 1M tokens (text / image / video), $0.30 / 1M tokens (audio)
- **Output price**: $0.40 / 1M tokens
- **Cached input price**: $0.01 / 1M tokens (text / image / video), $0.03 / 1M tokens (audio)
- **Capabilities**: vision, tool use, reasoning, audio

## Notes
- The Batch API offers a 50% cost reduction on requests.
- Context caching is available on the paid tier for select models to reduce input costs.
- A free tier is available with limited access to certain models.
- Deprecated models will be shut down after a notice period; users must migrate to newer models.
- Preview models may change before becoming stable and have more restrictive rate limits.
- Tokens for PDF documents are billed at the same rate as image tokens.
- Usage of Google AI Studio is free of charge in all available regions.
