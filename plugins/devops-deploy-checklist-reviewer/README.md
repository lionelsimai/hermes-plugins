# Deploy Checklist Reviewer

Deploy Checklist Reviewer for Hermes Agent: apply a analyze workflow to deploy checklist work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_deploy_checklist_reviewer` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_deploy_checklist_reviewer",
  "arguments": {
    "counts": {
      "deploy_checklist_risk_noted": 40,
      "deploy_checklist_rollback_step": 25,
      "deploy_checklist_verification": 10,
      "deploy_checklist_owner_named": 75
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
