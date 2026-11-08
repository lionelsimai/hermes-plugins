# Log Alert Review Checklist

Log Alert Review Checklist for Hermes Agent: apply a template workflow to log alert review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_log_alert_review_checklist` (kind: template)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_log_alert_review_checklist",
  "arguments": {
    "facts": {
      "log_alert_review_risk_noted": "Sample supplied fact",
      "log_alert_review_rollback_step": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
