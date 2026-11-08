# Nightly Backup Check Reporter

Nightly Backup Check Reporter for Hermes Agent: apply a score workflow to nightly backup check work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_nightly_backup_check_reporter` (kind: score)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_nightly_backup_check_reporter",
  "arguments": {
    "metrics": {
      "nightly_backup_check_schedule_clarity": 80,
      "nightly_backup_check_delivery_target": 65,
      "nightly_backup_check_failure_handling": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
