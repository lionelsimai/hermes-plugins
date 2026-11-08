# Whatsapp Broadcast Draft Checker

Whatsapp Broadcast Draft Checker for Hermes Agent: apply a score workflow to whatsapp broadcast draft work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_whatsapp_broadcast_draft_checker` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_whatsapp_broadcast_draft_checker",
  "arguments": {
    "metrics": {
      "whatsapp_broadcast_draft_audience_fit": 80,
      "whatsapp_broadcast_draft_tone_fit": 65,
      "whatsapp_broadcast_draft_length_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
