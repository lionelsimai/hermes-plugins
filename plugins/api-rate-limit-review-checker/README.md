# Rate Limit Review Checker

Rate Limit Review Checker for Hermes Agent: apply a template workflow to rate limit review work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rate_limit_review_checker` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rate_limit_review_checker",
  "arguments": {
    "facts": {
      "rate_limit_review_contract_fit": "Sample supplied fact",
      "rate_limit_review_auth_handled_safely": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
