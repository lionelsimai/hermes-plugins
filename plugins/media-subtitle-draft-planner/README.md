# Subtitle Draft Planner

Subtitle Draft Planner for Hermes Agent: apply a score workflow to subtitle draft work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_subtitle_draft_planner` (kind: score)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_subtitle_draft_planner",
  "arguments": {
    "metrics": {
      "subtitle_draft_brief_clarity": 80,
      "subtitle_draft_format_spec": 65,
      "subtitle_draft_rights_and_consent": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
