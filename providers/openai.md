---
provider: OpenAI
slug: openai
last_updated: 2026-05-18T15:35:15Z
sources:
  - https://openai.com/api/pricing/
  - https://platform.openai.com/docs/models
---

# OpenAI (GPT)

> Auto-generated from the official sources listed above. If something looks wrong, open an issue.

## Models

### GPT-5.5
- **Model ID**: `gpt-5.5`
- **Context window**: 1M tokens
- **Max output**: 128K tokens
- **Input price**: $5.00 / 1M tokens
- **Output price**: $30.00 / 1M tokens
- **Cached input price**: $0.50 / 1M tokens
- **Capabilities**: vision, tool use, reasoning
- **Knowledge cutoff**: Dec 1, 2025
- **Notes**: A new class of intelligence for coding and professional work.

### GPT-5.4
- **Model ID**: `gpt-5.4`
- **Context window**: 1M tokens
- **Max output**: 128K tokens
- **Input price**: $2.50 / 1M tokens
- **Output price**: $15.00 / 1M tokens
- **Cached input price**: $0.25 / 1M tokens
- **Capabilities**: vision, tool use, reasoning
- **Knowledge cutoff**: Aug 31, 2025
- **Notes**: A more affordable model for coding and professional work.

### GPT-5.4 mini
- **Model ID**: `gpt-5.4-mini`
- **Context window**: 400K tokens
- **Max output**: 128K tokens
- **Input price**: $0.75 / 1M tokens
- **Output price**: $4.50 / 1M tokens
- **Cached input price**: $0.075 / 1M tokens
- **Capabilities**: vision, tool use, reasoning
- **Knowledge cutoff**: Aug 31, 2025
- **Notes**: The strongest mini model for coding, computer use, and subagents.

### GPT-Image-2
- **Model ID**: `gpt-image-2`
- **Input price**:
    - Image: $8.00 / 1M tokens
    - Text: $5.00 / 1M tokens
- **Output price**: $30.00 / 1M tokens
- **Cached input price**:
    - Image: $2.00 / 1M tokens
    - Text: $1.25 / 1M tokens
- **Capabilities**: image generation
- **Notes**: State-of-the-art image generation model.

### GPT-Realtime-2
- **Model ID**: `gpt-realtime-2`
- **Input price**:
    - Audio: $32.00 / 1M tokens
    - Text: $4.00 / 1M tokens
    - Image: $5.00 / 1M tokens
- **Output price**:
    - Audio: $64.00 / 1M tokens
    - Text: $24.00 / 1M tokens
- **Cached input price**:
    - Audio: $0.40 / 1M tokens
    - Text: $0.40 / 1M tokens
    - Image: $0.50 / 1M tokens
- **Capabilities**: audio, vision, reasoning
- **Notes**: The most capable model for realtime voice interactions.

### GPT-Realtime-Translate
- **Model ID**: `gpt-realtime-translate`
- **Input price**: $0.034 per minute
- **Capabilities**: audio, translation
- **Notes**: A streaming speech-to-speech translation model.

### GPT-Realtime-Whisper
- **Model ID**: `gpt-realtime-whisper`
- **Input price**: $0.017 per minute
- **Capabilities**: audio, transcription
- **Notes**: A streaming speech-to-text model for realtime transcription.

## Notes
- The Batch API offers a 50% discount for asynchronous tasks completed within 24 hours.
- Prompt caching is available for several models, offering a significant discount on repeated input tokens.
- Fine-tuning is available for supervised, vision, and preference optimization tasks.
- Data residency options are available for enterprise customers, which adds 10% to the cost.
- Service tiers like Priority and Flex processing allow users to balance cost, speed, and availability.
- A list of deprecated models is maintained and can be consulted for model lifecycle information.
