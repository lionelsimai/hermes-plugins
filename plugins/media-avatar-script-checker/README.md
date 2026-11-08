# Avatar Script Checker

Avatar Script Checker for Hermes Agent: apply a score workflow to avatar script work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_avatar_script_checker` (kind: score)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_avatar_script_checker",
  "arguments": {
    "metrics": {
      "avatar_script_brief_clarity": 80,
      "avatar_script_format_spec": 65,
      "avatar_script_rights_and_consent": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
