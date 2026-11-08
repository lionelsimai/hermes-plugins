# Docker Review Reviewer

Docker Review Reviewer for Hermes Agent: apply a classify workflow to docker review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_docker_review_reviewer` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_docker_review_reviewer",
  "arguments": {
    "text": "Please review: this concerns docker review risk noted and docker review verification."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
