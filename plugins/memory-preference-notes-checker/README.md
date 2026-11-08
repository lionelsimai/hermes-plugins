# Preference Notes Checker

Preference Notes Checker for Hermes Agent: apply a analyze workflow to preference notes work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_preference_notes_checker` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_preference_notes_checker",
  "arguments": {
    "counts": {
      "preference_notes_fact_accuracy": 40,
      "preference_notes_size_budget_fit": 25,
      "preference_notes_staleness": 10,
      "preference_notes_duplication": 75
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
