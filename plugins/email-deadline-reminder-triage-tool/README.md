# Deadline Reminder Triage Tool

Deadline Reminder Triage Tool for Hermes Agent: apply a audit workflow to deadline reminder work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_deadline_reminder_triage_tool` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_deadline_reminder_triage_tool",
  "arguments": {
    "text": "This sample covers deadline reminder priority accuracy and deadline reminder tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
