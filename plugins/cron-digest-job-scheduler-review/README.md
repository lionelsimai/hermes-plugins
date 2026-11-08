# Digest Job Scheduler Review

Digest Job Scheduler Review for Hermes Agent: apply a analyze workflow to digest job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_digest_job_scheduler_review` (kind: analyze)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_digest_job_scheduler_review",
  "arguments": {
    "counts": {
      "digest_job_schedule_clarity": 40,
      "digest_job_delivery_target": 25,
      "digest_job_failure_handling": 10,
      "digest_job_idempotency": 75
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
