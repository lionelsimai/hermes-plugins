# Reminder Job Reporter

Reminder Job Reporter for Hermes Agent: apply a template workflow to reminder job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_reminder_job_reporter` (kind: template)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_reminder_job_reporter",
  "arguments": {
    "facts": {
      "reminder_job_schedule_clarity": "Sample supplied fact",
      "reminder_job_delivery_target": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
