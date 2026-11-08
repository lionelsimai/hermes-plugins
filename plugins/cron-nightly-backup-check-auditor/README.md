# Nightly Backup Check Auditor

Nightly Backup Check Auditor for Hermes Agent: apply a audit workflow to nightly backup check work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_nightly_backup_check_auditor` (kind: audit)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_nightly_backup_check_auditor",
  "arguments": {
    "text": "This sample covers nightly backup check schedule clarity and nightly backup check delivery target in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
