# Travel Hold Triage Tool

Travel Hold Triage Tool for Hermes Agent: apply a score workflow to travel hold work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_travel_hold_triage_tool` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_travel_hold_triage_tool",
  "arguments": {
    "metrics": {
      "travel_hold_priority_accuracy": 80,
      "travel_hold_tone_fit": 65,
      "travel_hold_facts_supplied_only": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
