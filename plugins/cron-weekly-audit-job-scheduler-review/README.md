# Weekly Audit Job Scheduler Review

Weekly Audit Job Scheduler Review for Hermes Agent: apply a classify workflow to weekly audit job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_weekly_audit_job_scheduler_review` (kind: classify)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_weekly_audit_job_scheduler_review",
  "arguments": {
    "text": "Please review: this concerns weekly audit job schedule clarity and weekly audit job failure handling."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
