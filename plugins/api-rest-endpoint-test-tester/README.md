# Rest Endpoint Test Tester

Rest Endpoint Test Tester for Hermes Agent: apply a template workflow to rest endpoint test work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rest_endpoint_test_tester` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rest_endpoint_test_tester",
  "arguments": {
    "facts": {
      "rest_endpoint_test_contract_fit": "Sample supplied fact",
      "rest_endpoint_test_auth_handled_safely": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
