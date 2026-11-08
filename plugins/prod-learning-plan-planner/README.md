# Learning Plan Planner

Learning Plan Planner for Hermes Agent: apply a classify workflow to learning plan work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_learning_plan_planner` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_learning_plan_planner",
  "arguments": {
    "text": "Please review: this concerns learning plan priority clarity and learning plan next action named."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
