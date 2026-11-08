# Lesson Learned Auditor

Lesson Learned Auditor for Hermes Agent: apply a analyze workflow to lesson learned work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_lesson_learned_auditor` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_lesson_learned_auditor",
  "arguments": {
    "counts": {
      "lesson_learned_fact_accuracy": 40,
      "lesson_learned_size_budget_fit": 25,
      "lesson_learned_staleness": 10,
      "lesson_learned_duplication": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
