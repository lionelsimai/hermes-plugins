# Reading List Tracker

Reading List Tracker for Hermes Agent: apply a analyze workflow to reading list work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_reading_list_tracker` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_reading_list_tracker",
  "arguments": {
    "counts": {
      "reading_list_priority_clarity": 40,
      "reading_list_time_realism": 25,
      "reading_list_next_action_named": 10,
      "reading_list_review_cadence": 75
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
