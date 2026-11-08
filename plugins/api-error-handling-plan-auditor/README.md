# Error Handling Plan Auditor

Error Handling Plan Auditor for Hermes Agent: apply a score workflow to error handling plan work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_error_handling_plan_auditor` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_error_handling_plan_auditor",
  "arguments": {
    "metrics": {
      "error_handling_plan_contract_fit": 80,
      "error_handling_plan_auth_handled_safely": 65,
      "error_handling_plan_error_cases_covered": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
