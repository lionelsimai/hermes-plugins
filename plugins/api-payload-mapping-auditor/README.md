# Payload Mapping Auditor

Payload Mapping Auditor for Hermes Agent: apply a classify workflow to payload mapping work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_payload_mapping_auditor` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_payload_mapping_auditor",
  "arguments": {
    "text": "Please review: this concerns payload mapping contract fit and payload mapping error cases covered."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
