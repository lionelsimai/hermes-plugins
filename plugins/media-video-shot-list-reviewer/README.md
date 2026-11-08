# Video Shot List Reviewer

Video Shot List Reviewer for Hermes Agent: apply a audit workflow to video shot list work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_video_shot_list_reviewer` (kind: audit)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_video_shot_list_reviewer",
  "arguments": {
    "text": "This sample covers video shot list brief clarity and video shot list format spec in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
