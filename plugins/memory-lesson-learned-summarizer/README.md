# Lesson Learned Summarizer

Lesson Learned Summarizer for Hermes Agent: apply a classify workflow to lesson learned work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_lesson_learned_summarizer` (kind: classify)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_lesson_learned_summarizer",
  "arguments": {
    "text": "Please review: this concerns lesson learned fact accuracy and lesson learned staleness."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
