# Channel Summary Drafter

Channel Summary Drafter for Hermes Agent: apply a checklist workflow to channel summary work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_channel_summary_drafter` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_channel_summary_drafter",
  "arguments": {
    "completed": [
      "channel summary audience fit",
      "channel summary tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
