# Report Delivery Reporter

Report Delivery Reporter for Hermes Agent: apply a analyze workflow to report delivery work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_report_delivery_reporter` (kind: analyze)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_report_delivery_reporter",
  "arguments": {
    "counts": {
      "report_delivery_schedule_clarity": 40,
      "report_delivery_delivery_target": 25,
      "report_delivery_failure_handling": 10,
      "report_delivery_idempotency": 75
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
