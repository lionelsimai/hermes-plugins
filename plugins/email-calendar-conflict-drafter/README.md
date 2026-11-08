# Calendar Conflict Drafter

Calendar Conflict Drafter for Hermes Agent: apply a score workflow to calendar conflict work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_calendar_conflict_drafter` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_calendar_conflict_drafter",
  "arguments": {
    "metrics": {
      "calendar_conflict_priority_accuracy": 80,
      "calendar_conflict_tone_fit": 65,
      "calendar_conflict_facts_supplied_only": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
