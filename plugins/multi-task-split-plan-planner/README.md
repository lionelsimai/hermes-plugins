# Task Split Plan Planner

Task Split Plan Planner for Hermes Agent: apply a classify workflow to task split plan work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_task_split_plan_planner` (kind: classify)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_task_split_plan_planner",
  "arguments": {
    "text": "Please review: this concerns task split plan scope clarity and task split plan merge criteria."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
