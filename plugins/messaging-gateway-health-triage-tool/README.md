# Gateway Health Triage Tool

Gateway Health Triage Tool for Hermes Agent: apply a classify workflow to gateway health work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_gateway_health_triage_tool` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_gateway_health_triage_tool",
  "arguments": {
    "text": "Please review: this concerns gateway health audience fit and gateway health length fit."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
