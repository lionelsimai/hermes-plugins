# Rate Limit Review Mapper

Rate Limit Review Mapper for Hermes Agent: apply a score workflow to rate limit review work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rate_limit_review_mapper` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rate_limit_review_mapper",
  "arguments": {
    "metrics": {
      "rate_limit_review_contract_fit": 80,
      "rate_limit_review_auth_handled_safely": 65,
      "rate_limit_review_error_cases_covered": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
