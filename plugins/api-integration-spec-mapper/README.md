# Integration Spec Mapper

Integration Spec Mapper for Hermes Agent: apply a template workflow to integration spec work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_integration_spec_mapper` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_integration_spec_mapper",
  "arguments": {
    "facts": {
      "integration_spec_contract_fit": "Sample supplied fact",
      "integration_spec_auth_handled_safely": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
