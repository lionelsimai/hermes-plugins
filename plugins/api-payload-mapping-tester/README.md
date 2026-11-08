# Payload Mapping Tester

Payload Mapping Tester for Hermes Agent: apply a checklist workflow to payload mapping work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_payload_mapping_tester` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_payload_mapping_tester",
  "arguments": {
    "completed": [
      "payload mapping contract fit",
      "payload mapping auth handled safely"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
