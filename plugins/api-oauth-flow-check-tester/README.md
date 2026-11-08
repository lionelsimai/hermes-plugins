# Oauth Flow Check Tester

Oauth Flow Check Tester for Hermes Agent: apply a analyze workflow to oauth flow check work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_oauth_flow_check_tester` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_oauth_flow_check_tester",
  "arguments": {
    "counts": {
      "oauth_flow_check_contract_fit": 40,
      "oauth_flow_check_auth_handled_safely": 25,
      "oauth_flow_check_error_cases_covered": 10,
      "oauth_flow_check_rate_limits_respected": 75
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
