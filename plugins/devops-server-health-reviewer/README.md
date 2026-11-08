# Server Health Reviewer

Server Health Reviewer for Hermes Agent: apply a score workflow to server health work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_server_health_reviewer` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_server_health_reviewer",
  "arguments": {
    "metrics": {
      "server_health_risk_noted": 80,
      "server_health_rollback_step": 65,
      "server_health_verification": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
