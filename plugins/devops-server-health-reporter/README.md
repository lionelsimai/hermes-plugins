# Server Health Reporter

Server Health Reporter for Hermes Agent: apply a analyze workflow to server health work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_server_health_reporter` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_server_health_reporter",
  "arguments": {
    "counts": {
      "server_health_risk_noted": 40,
      "server_health_rollback_step": 25,
      "server_health_verification": 10,
      "server_health_owner_named": 75
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
