# Habit Tracker Planner

Habit Tracker Planner for Hermes Agent: apply a analyze workflow to habit tracker work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_habit_tracker_planner` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_habit_tracker_planner",
  "arguments": {
    "counts": {
      "habit_tracker_priority_clarity": 40,
      "habit_tracker_time_realism": 25,
      "habit_tracker_next_action_named": 10,
      "habit_tracker_review_cadence": 75
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
