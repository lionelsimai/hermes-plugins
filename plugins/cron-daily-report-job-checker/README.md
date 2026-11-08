# Daily Report Job Checker

Daily Report Job Checker for Hermes Agent: apply a checklist workflow to daily report job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_daily_report_job_checker` (kind: checklist)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_daily_report_job_checker",
  "arguments": {
    "completed": [
      "daily report job schedule clarity",
      "daily report job delivery target"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
