# Learning Plan Drafter

Learning Plan Drafter for Hermes Agent: apply a score workflow to learning plan work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_learning_plan_drafter` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_learning_plan_drafter",
  "arguments": {
    "metrics": {
      "learning_plan_priority_clarity": 80,
      "learning_plan_time_realism": 65,
      "learning_plan_next_action_named": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
