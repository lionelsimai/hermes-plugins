# Ci Pipeline Check Planner

Ci Pipeline Check Planner for Hermes Agent: apply a checklist workflow to ci pipeline check work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_ci_pipeline_check_planner` (kind: checklist)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_ci_pipeline_check_planner",
  "arguments": {
    "completed": [
      "ci pipeline check risk noted",
      "ci pipeline check rollback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
