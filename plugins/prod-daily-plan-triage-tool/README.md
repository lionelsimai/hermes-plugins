# Daily Plan Triage Tool

Daily Plan Triage Tool for Hermes Agent: apply a score workflow to daily plan work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_daily_plan_triage_tool` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_daily_plan_triage_tool",
  "arguments": {
    "metrics": {
      "daily_plan_priority_clarity": 80,
      "daily_plan_time_realism": 65,
      "daily_plan_next_action_named": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
