# Travel Plan Planner

Travel Plan Planner for Hermes Agent: apply a template workflow to travel plan work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_travel_plan_planner` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_travel_plan_planner",
  "arguments": {
    "facts": {
      "travel_plan_priority_clarity": "Sample supplied fact",
      "travel_plan_time_realism": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
