# Dns Change Plan Reporter

Dns Change Plan Reporter for Hermes Agent: apply a classify workflow to dns change plan work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_dns_change_plan_reporter` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_dns_change_plan_reporter",
  "arguments": {
    "text": "Please review: this concerns dns change plan risk noted and dns change plan verification."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
