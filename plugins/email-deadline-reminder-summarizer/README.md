# Deadline Reminder Summarizer

Deadline Reminder Summarizer for Hermes Agent: apply a checklist workflow to deadline reminder work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_deadline_reminder_summarizer` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_deadline_reminder_summarizer",
  "arguments": {
    "completed": [
      "deadline reminder priority accuracy",
      "deadline reminder tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
