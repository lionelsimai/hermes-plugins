# Whatsapp Broadcast Draft Planner

Whatsapp Broadcast Draft Planner for Hermes Agent: apply a checklist workflow to whatsapp broadcast draft work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_whatsapp_broadcast_draft_planner` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_whatsapp_broadcast_draft_planner",
  "arguments": {
    "completed": [
      "whatsapp broadcast draft audience fit",
      "whatsapp broadcast draft tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
