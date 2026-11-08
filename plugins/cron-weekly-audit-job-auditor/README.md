# Weekly Audit Job Auditor

Weekly Audit Job Auditor for Hermes Agent: apply a template workflow to weekly audit job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_weekly_audit_job_auditor` (kind: template)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_weekly_audit_job_auditor",
  "arguments": {
    "facts": {
      "weekly_audit_job_schedule_clarity": "Sample supplied fact",
      "weekly_audit_job_delivery_target": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
