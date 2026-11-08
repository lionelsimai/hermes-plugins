# Video Shot List Planner

Video Shot List Planner for Hermes Agent: apply a analyze workflow to video shot list work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_video_shot_list_planner` (kind: analyze)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_video_shot_list_planner",
  "arguments": {
    "counts": {
      "video_shot_list_brief_clarity": 40,
      "video_shot_list_format_spec": 25,
      "video_shot_list_rights_and_consent": 10,
      "video_shot_list_quality_gate": 75
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
