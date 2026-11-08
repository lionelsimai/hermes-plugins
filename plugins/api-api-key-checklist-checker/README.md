# Api Key Checklist Checker

Api Key Checklist Checker for Hermes Agent: apply a score workflow to api key checklist work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_api_key_checklist_checker` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_api_key_checklist_checker",
  "arguments": {
    "metrics": {
      "api_key_checklist_contract_fit": 80,
      "api_key_checklist_auth_handled_safely": 65,
      "api_key_checklist_error_cases_covered": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
