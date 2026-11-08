# Focus Block Reviewer

Focus Block Reviewer for Hermes Agent: apply a analyze workflow to focus block work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_focus_block_reviewer` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_focus_block_reviewer",
  "arguments": {
    "counts": {
      "focus_block_priority_clarity": 40,
      "focus_block_time_realism": 25,
      "focus_block_next_action_named": 10,
      "focus_block_review_cadence": 75
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
