# Dm Triage Triage Tool

Dm Triage Triage Tool for Hermes Agent: apply a audit workflow to dm triage work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_dm_triage_triage_tool` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_dm_triage_triage_tool",
  "arguments": {
    "text": "This sample covers dm triage audience fit and dm triage tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
