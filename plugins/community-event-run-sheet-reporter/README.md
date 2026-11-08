# Event Run Sheet Reporter

Event Run Sheet Reporter for Hermes Agent: apply a template workflow to event run sheet work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_event_run_sheet_reporter` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_event_run_sheet_reporter",
  "arguments": {
    "facts": {
      "event_run_sheet_member_fit": "Sample supplied fact",
      "event_run_sheet_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
