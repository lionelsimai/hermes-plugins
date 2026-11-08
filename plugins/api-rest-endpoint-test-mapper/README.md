# Rest Endpoint Test Mapper

Rest Endpoint Test Mapper for Hermes Agent: apply a classify workflow to rest endpoint test work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rest_endpoint_test_mapper` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rest_endpoint_test_mapper",
  "arguments": {
    "text": "Please review: this concerns rest endpoint test contract fit and rest endpoint test error cases covered."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
