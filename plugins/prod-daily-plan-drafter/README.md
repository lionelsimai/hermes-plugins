# Daily Plan Drafter

Daily Plan Drafter for Hermes Agent: apply a analyze workflow to daily plan work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_daily_plan_drafter` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_daily_plan_drafter",
  "arguments": {
    "counts": {
      "daily_plan_priority_clarity": 40,
      "daily_plan_time_realism": 25,
      "daily_plan_next_action_named": 10,
      "daily_plan_review_cadence": 75
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
