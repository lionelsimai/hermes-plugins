# Report Delivery Scheduler Review

Report Delivery Scheduler Review for Hermes Agent: apply a template workflow to report delivery work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_report_delivery_scheduler_review` (kind: template)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_report_delivery_scheduler_review",
  "arguments": {
    "facts": {
      "report_delivery_schedule_clarity": "Sample supplied fact",
      "report_delivery_delivery_target": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
