# Thumbnail Plan Planner

Thumbnail Plan Planner for Hermes Agent: apply a classify workflow to thumbnail plan work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_thumbnail_plan_planner` (kind: classify)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_thumbnail_plan_planner",
  "arguments": {
    "text": "Please review: this concerns thumbnail plan brief clarity and thumbnail plan rights and consent."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
