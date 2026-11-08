# Cleanup Job Scheduler Review

Cleanup Job Scheduler Review for Hermes Agent: apply a score workflow to cleanup job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_cleanup_job_scheduler_review` (kind: score)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_cleanup_job_scheduler_review",
  "arguments": {
    "metrics": {
      "cleanup_job_schedule_clarity": 80,
      "cleanup_job_delivery_target": 65,
      "cleanup_job_failure_handling": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
