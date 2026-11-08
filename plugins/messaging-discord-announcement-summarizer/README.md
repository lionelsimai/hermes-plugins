# Discord Announcement Summarizer

Discord Announcement Summarizer for Hermes Agent: apply a audit workflow to discord announcement work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_discord_announcement_summarizer` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_discord_announcement_summarizer",
  "arguments": {
    "text": "This sample covers discord announcement audience fit and discord announcement tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
