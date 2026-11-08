# Gateway Health Drafter

Gateway Health Drafter for Hermes Agent: apply a analyze workflow to gateway health work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_gateway_health_drafter` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_gateway_health_drafter",
  "arguments": {
    "counts": {
      "gateway_health_audience_fit": 40,
      "gateway_health_tone_fit": 25,
      "gateway_health_length_fit": 10,
      "gateway_health_approval_gate": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
