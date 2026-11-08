# Weekly Audit Job Checker

Weekly Audit Job Checker for Hermes Agent: apply a analyze workflow to weekly audit job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_weekly_audit_job_checker` (kind: analyze)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_weekly_audit_job_checker",
  "arguments": {
    "counts": {
      "weekly_audit_job_schedule_clarity": 40,
      "weekly_audit_job_delivery_target": 25,
      "weekly_audit_job_failure_handling": 10,
      "weekly_audit_job_idempotency": 75
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
