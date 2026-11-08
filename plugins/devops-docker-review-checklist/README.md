# Docker Review Checklist

Docker Review Checklist for Hermes Agent: apply a analyze workflow to docker review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_docker_review_checklist` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_docker_review_checklist",
  "arguments": {
    "counts": {
      "docker_review_risk_noted": 40,
      "docker_review_rollback_step": 25,
      "docker_review_verification": 10,
      "docker_review_owner_named": 75
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
