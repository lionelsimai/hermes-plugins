# Dm Triage Drafter

Dm Triage Drafter for Hermes Agent: apply a classify workflow to dm triage work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_dm_triage_drafter` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_dm_triage_drafter",
  "arguments": {
    "text": "Please review: this concerns dm triage audience fit and dm triage length fit."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
