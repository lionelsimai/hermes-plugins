# Daily Plan Tracker

Daily Plan Tracker for Hermes Agent: apply a template workflow to daily plan work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_daily_plan_tracker` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_daily_plan_tracker",
  "arguments": {
    "facts": {
      "daily_plan_priority_clarity": "Sample supplied fact",
      "daily_plan_time_realism": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
