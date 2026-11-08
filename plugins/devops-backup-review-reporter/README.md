# Backup Review Reporter

Backup Review Reporter for Hermes Agent: apply a score workflow to backup review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_backup_review_reporter` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_backup_review_reporter",
  "arguments": {
    "metrics": {
      "backup_review_risk_noted": 80,
      "backup_review_rollback_step": 65,
      "backup_review_verification": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
