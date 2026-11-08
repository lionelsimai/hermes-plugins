# Meeting Agenda Checker

Meeting Agenda Checker for Hermes Agent: apply a score workflow to meeting agenda work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_meeting_agenda_checker` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_meeting_agenda_checker",
  "arguments": {
    "metrics": {
      "meeting_agenda_priority_accuracy": 80,
      "meeting_agenda_tone_fit": 65,
      "meeting_agenda_facts_supplied_only": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
