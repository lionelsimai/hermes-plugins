# Subtitle Draft Checker

Subtitle Draft Checker for Hermes Agent: apply a checklist workflow to subtitle draft work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_subtitle_draft_checker` (kind: checklist)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_subtitle_draft_checker",
  "arguments": {
    "completed": [
      "subtitle draft brief clarity",
      "subtitle draft format spec"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
