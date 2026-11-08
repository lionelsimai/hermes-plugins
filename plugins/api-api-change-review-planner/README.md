# Api Change Review Planner

Api Change Review Planner for Hermes Agent: apply a score workflow to api change review work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_api_change_review_planner` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_api_change_review_planner",
  "arguments": {
    "metrics": {
      "api_change_review_contract_fit": 80,
      "api_change_review_auth_handled_safely": 65,
      "api_change_review_error_cases_covered": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
