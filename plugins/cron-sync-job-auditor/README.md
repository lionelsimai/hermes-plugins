# Sync Job Auditor

Sync Job Auditor for Hermes Agent: apply a analyze workflow to sync job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_sync_job_auditor` (kind: analyze)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_sync_job_auditor",
  "arguments": {
    "counts": {
      "sync_job_schedule_clarity": 40,
      "sync_job_delivery_target": 25,
      "sync_job_failure_handling": 10,
      "sync_job_idempotency": 75
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
