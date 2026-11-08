# Monitoring Job Checker

Monitoring Job Checker for Hermes Agent: apply a audit workflow to monitoring job work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_monitoring_job_checker` (kind: audit)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_monitoring_job_checker",
  "arguments": {
    "text": "This sample covers monitoring job schedule clarity and monitoring job delivery target in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
