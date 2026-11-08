# Podcast Outline Drafter

Podcast Outline Drafter for Hermes Agent: apply a audit workflow to podcast outline work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_podcast_outline_drafter` (kind: audit)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_podcast_outline_drafter",
  "arguments": {
    "text": "This sample covers podcast outline brief clarity and podcast outline format spec in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
