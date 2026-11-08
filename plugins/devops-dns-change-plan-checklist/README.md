# Dns Change Plan Checklist

Dns Change Plan Checklist for Hermes Agent: apply a score workflow to dns change plan work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_dns_change_plan_checklist` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_dns_change_plan_checklist",
  "arguments": {
    "metrics": {
      "dns_change_plan_risk_noted": 80,
      "dns_change_plan_rollback_step": 65,
      "dns_change_plan_verification": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
