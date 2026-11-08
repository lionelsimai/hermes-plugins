# Dns Change Plan Planner

Dns Change Plan Planner for Hermes Agent: apply a analyze workflow to dns change plan work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_dns_change_plan_planner` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_dns_change_plan_planner",
  "arguments": {
    "counts": {
      "dns_change_plan_risk_noted": 40,
      "dns_change_plan_rollback_step": 25,
      "dns_change_plan_verification": 10,
      "dns_change_plan_owner_named": 75
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
