# Report Delivery Checker

Report Delivery Checker for Hermes Agent: apply a checklist workflow to report delivery work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_report_delivery_checker` (kind: checklist)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_report_delivery_checker",
  "arguments": {
    "completed": [
      "report delivery schedule clarity",
      "report delivery delivery target"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
