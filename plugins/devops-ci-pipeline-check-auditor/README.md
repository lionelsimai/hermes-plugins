# Ci Pipeline Check Auditor

Ci Pipeline Check Auditor for Hermes Agent: apply a score workflow to ci pipeline check work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_ci_pipeline_check_auditor` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_ci_pipeline_check_auditor",
  "arguments": {
    "metrics": {
      "ci_pipeline_check_risk_noted": 80,
      "ci_pipeline_check_rollback_step": 65,
      "ci_pipeline_check_verification": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
