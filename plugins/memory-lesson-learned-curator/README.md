# Lesson Learned Curator

Lesson Learned Curator for Hermes Agent: apply a template workflow to lesson learned work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_lesson_learned_curator` (kind: template)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_lesson_learned_curator",
  "arguments": {
    "facts": {
      "lesson_learned_fact_accuracy": "Sample supplied fact",
      "lesson_learned_size_budget_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
