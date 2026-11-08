# Dns Change Plan Reviewer

Dns Change Plan Reviewer for Hermes Agent: apply a checklist workflow to dns change plan work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_dns_change_plan_reviewer` (kind: checklist)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_dns_change_plan_reviewer",
  "arguments": {
    "completed": [
      "dns change plan risk noted",
      "dns change plan rollback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
