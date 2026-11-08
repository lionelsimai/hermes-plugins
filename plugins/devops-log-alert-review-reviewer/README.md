# Log Alert Review Reviewer

Log Alert Review Reviewer for Hermes Agent: apply a analyze workflow to log alert review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_log_alert_review_reviewer` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_log_alert_review_reviewer",
  "arguments": {
    "counts": {
      "log_alert_review_risk_noted": 40,
      "log_alert_review_rollback_step": 25,
      "log_alert_review_verification": 10,
      "log_alert_review_owner_named": 75
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
