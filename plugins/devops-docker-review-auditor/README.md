# Docker Review Auditor

Docker Review Auditor for Hermes Agent: apply a audit workflow to docker review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_docker_review_auditor` (kind: audit)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_docker_review_auditor",
  "arguments": {
    "text": "This sample covers docker review risk noted and docker review rollback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
