# Cost Review Reporter

Cost Review Reporter for Hermes Agent: apply a analyze workflow to cost review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_cost_review_reporter` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_cost_review_reporter",
  "arguments": {
    "counts": {
      "cost_review_risk_noted": 40,
      "cost_review_rollback_step": 25,
      "cost_review_verification": 10,
      "cost_review_owner_named": 75
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
