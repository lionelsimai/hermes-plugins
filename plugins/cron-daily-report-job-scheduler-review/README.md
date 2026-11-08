# Daily Report Job Scheduler Review

Daily Report Job Scheduler Review for Hermes Agent: apply a template workflow to daily report job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_daily_report_job_scheduler_review` (kind: template)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_daily_report_job_scheduler_review",
  "arguments": {
    "facts": {
      "daily_report_job_schedule_clarity": "Sample supplied fact",
      "daily_report_job_delivery_target": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
