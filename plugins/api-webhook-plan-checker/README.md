# Webhook Plan Checker

Webhook Plan Checker for Hermes Agent: apply a analyze workflow to webhook plan work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_webhook_plan_checker` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_webhook_plan_checker",
  "arguments": {
    "counts": {
      "webhook_plan_contract_fit": 40,
      "webhook_plan_auth_handled_safely": 25,
      "webhook_plan_error_cases_covered": 10,
      "webhook_plan_rate_limits_respected": 75
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
