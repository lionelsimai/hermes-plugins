# Weekly Audit Job Reporter

Weekly Audit Job Reporter for Hermes Agent: apply a audit workflow to weekly audit job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_weekly_audit_job_reporter` (kind: audit)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_weekly_audit_job_reporter",
  "arguments": {
    "text": "This sample covers weekly audit job schedule clarity and weekly audit job delivery target in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
