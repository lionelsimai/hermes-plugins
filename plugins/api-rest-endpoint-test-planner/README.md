# Rest Endpoint Test Planner

Rest Endpoint Test Planner for Hermes Agent: apply a analyze workflow to rest endpoint test work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rest_endpoint_test_planner` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rest_endpoint_test_planner",
  "arguments": {
    "counts": {
      "rest_endpoint_test_contract_fit": 40,
      "rest_endpoint_test_auth_handled_safely": 25,
      "rest_endpoint_test_error_cases_covered": 10,
      "rest_endpoint_test_rate_limits_respected": 75
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
