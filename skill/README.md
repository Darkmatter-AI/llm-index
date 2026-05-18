# llm-index skill

Tells Claude Code (and other Anthropic-SDK agents that read SKILL.md files) to consult [darkmatter-ai.github.io/llm-index](https://darkmatter-ai.github.io/llm-index/) for current LLM model and pricing data instead of relying on training-cutoff knowledge.

## Install (user-level, per-machine)

```bash
mkdir -p ~/.claude/skills/llm-index
curl -fsSL https://raw.githubusercontent.com/darkmatter-ai/llm-index/main/skill/SKILL.md \
  -o ~/.claude/skills/llm-index/SKILL.md
```

Restart your Claude Code session. The skill is now listed in `/help` and will activate automatically when you ask model/pricing questions.

## Install (project-level)

```bash
mkdir -p .claude/skills/llm-index
curl -fsSL https://raw.githubusercontent.com/darkmatter-ai/llm-index/main/skill/SKILL.md \
  -o .claude/skills/llm-index/SKILL.md
```

Commit `.claude/skills/llm-index/SKILL.md` so the whole team picks it up.

## Update

The skill itself almost never changes — the data behind it (on the site) refreshes weekly. If you want to pull the latest skill instructions, re-run the install command.

## Uninstall

```bash
rm -rf ~/.claude/skills/llm-index           # user-level
rm -rf .claude/skills/llm-index             # project-level
```
