# Travel Hold Planner

Travel Hold Planner for Hermes Agent: apply a analyze workflow to travel hold work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_travel_hold_planner` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_travel_hold_planner",
  "arguments": {
    "counts": {
      "travel_hold_priority_accuracy": 40,
      "travel_hold_tone_fit": 25,
      "travel_hold_facts_supplied_only": 10,
      "travel_hold_approval_gate": 75
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
