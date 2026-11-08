# Preference Notes Curator

Preference Notes Curator for Hermes Agent: apply a score workflow to preference notes work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_preference_notes_curator` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_preference_notes_curator",
  "arguments": {
    "metrics": {
      "preference_notes_fact_accuracy": 80,
      "preference_notes_size_budget_fit": 65,
      "preference_notes_staleness": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
