# Reading List Planner

Reading List Planner for Hermes Agent: apply a score workflow to reading list work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_reading_list_planner` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_reading_list_planner",
  "arguments": {
    "metrics": {
      "reading_list_priority_clarity": 80,
      "reading_list_time_realism": 65,
      "reading_list_next_action_named": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
