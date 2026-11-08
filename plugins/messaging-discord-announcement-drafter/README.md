# Discord Announcement Drafter

Discord Announcement Drafter for Hermes Agent: apply a analyze workflow to discord announcement work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_discord_announcement_drafter` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_discord_announcement_drafter",
  "arguments": {
    "counts": {
      "discord_announcement_audience_fit": 40,
      "discord_announcement_tone_fit": 25,
      "discord_announcement_length_fit": 10,
      "discord_announcement_approval_gate": 75
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
