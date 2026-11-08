# Report Delivery Auditor

Report Delivery Auditor for Hermes Agent: apply a score workflow to report delivery work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_report_delivery_auditor` (kind: score)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_report_delivery_auditor",
  "arguments": {
    "metrics": {
      "report_delivery_schedule_clarity": 80,
      "report_delivery_delivery_target": 65,
      "report_delivery_failure_handling": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
