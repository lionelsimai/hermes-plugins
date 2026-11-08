# Audio Cleanup Plan Briefer

Audio Cleanup Plan Briefer for Hermes Agent: apply a analyze workflow to audio cleanup plan work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_audio_cleanup_plan_briefer` (kind: analyze)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_audio_cleanup_plan_briefer",
  "arguments": {
    "counts": {
      "audio_cleanup_plan_brief_clarity": 40,
      "audio_cleanup_plan_format_spec": 25,
      "audio_cleanup_plan_rights_and_consent": 10,
      "audio_cleanup_plan_quality_gate": 75
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
