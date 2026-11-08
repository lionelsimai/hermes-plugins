# Thumbnail Plan Checker

Thumbnail Plan Checker for Hermes Agent: apply a audit workflow to thumbnail plan work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_thumbnail_plan_checker` (kind: audit)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_thumbnail_plan_checker",
  "arguments": {
    "text": "This sample covers thumbnail plan brief clarity and thumbnail plan format spec in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
