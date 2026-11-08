# Task List Triage Drafter

Task List Triage Drafter for Hermes Agent: apply a score workflow to task list triage work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_task_list_triage_drafter` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_task_list_triage_drafter",
  "arguments": {
    "metrics": {
      "task_list_triage_priority_clarity": 80,
      "task_list_triage_time_realism": 65,
      "task_list_triage_next_action_named": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
