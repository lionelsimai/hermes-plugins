# Voiceover Script Checker

Voiceover Script Checker for Hermes Agent: apply a template workflow to voiceover script work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_voiceover_script_checker` (kind: template)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_voiceover_script_checker",
  "arguments": {
    "facts": {
      "voiceover_script_brief_clarity": "Sample supplied fact",
      "voiceover_script_format_spec": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
