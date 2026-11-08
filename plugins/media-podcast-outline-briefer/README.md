# Podcast Outline Briefer

Podcast Outline Briefer for Hermes Agent: apply a classify workflow to podcast outline work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_podcast_outline_briefer` (kind: classify)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_podcast_outline_briefer",
  "arguments": {
    "text": "Please review: this concerns podcast outline brief clarity and podcast outline rights and consent."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
