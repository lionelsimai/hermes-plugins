# Task Split Plan Reviewer

Task Split Plan Reviewer for Hermes Agent: apply a score workflow to task split plan work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_task_split_plan_reviewer` (kind: score)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_task_split_plan_reviewer",
  "arguments": {
    "metrics": {
      "task_split_plan_scope_clarity": 80,
      "task_split_plan_independence_of_subtasks": 65,
      "task_split_plan_merge_criteria": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
