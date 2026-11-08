# Audio Cleanup Plan Drafter

Audio Cleanup Plan Drafter for Hermes Agent: apply a classify workflow to audio cleanup plan work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_audio_cleanup_plan_drafter` (kind: classify)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_audio_cleanup_plan_drafter",
  "arguments": {
    "text": "Please review: this concerns audio cleanup plan brief clarity and audio cleanup plan rights and consent."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
