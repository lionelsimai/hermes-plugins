# Api Change Review Checker

Api Change Review Checker for Hermes Agent: apply a analyze workflow to api change review work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_api_change_review_checker` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_api_change_review_checker",
  "arguments": {
    "counts": {
      "api_change_review_contract_fit": 40,
      "api_change_review_auth_handled_safely": 25,
      "api_change_review_error_cases_covered": 10,
      "api_change_review_rate_limits_respected": 75
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
