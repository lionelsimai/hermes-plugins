# Webhook Plan Planner

Webhook Plan Planner for Hermes Agent: apply a score workflow to webhook plan work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_webhook_plan_planner` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_webhook_plan_planner",
  "arguments": {
    "metrics": {
      "webhook_plan_contract_fit": 80,
      "webhook_plan_auth_handled_safely": 65,
      "webhook_plan_error_cases_covered": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
