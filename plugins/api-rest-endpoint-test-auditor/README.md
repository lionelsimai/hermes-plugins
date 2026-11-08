# Rest Endpoint Test Auditor

Rest Endpoint Test Auditor for Hermes Agent: apply a audit workflow to rest endpoint test work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rest_endpoint_test_auditor` (kind: audit)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rest_endpoint_test_auditor",
  "arguments": {
    "text": "This sample covers rest endpoint test contract fit and rest endpoint test auth handled safely in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
