# Deploy Checklist Checklist

Deploy Checklist Checklist for Hermes Agent: apply a template workflow to deploy checklist work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_deploy_checklist_checklist` (kind: template)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_deploy_checklist_checklist",
  "arguments": {
    "facts": {
      "deploy_checklist_risk_noted": "Sample supplied fact",
      "deploy_checklist_rollback_step": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
