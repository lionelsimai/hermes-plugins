# Reminder Job Checker

Reminder Job Checker for Hermes Agent: apply a score workflow to reminder job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_reminder_job_checker` (kind: score)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_reminder_job_checker",
  "arguments": {
    "metrics": {
      "reminder_job_schedule_clarity": 80,
      "reminder_job_delivery_target": 65,
      "reminder_job_failure_handling": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
