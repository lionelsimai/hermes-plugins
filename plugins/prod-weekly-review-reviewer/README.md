# Weekly Review Reviewer

Weekly Review Reviewer for Hermes Agent: apply a score workflow to weekly review work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_weekly_review_reviewer` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_weekly_review_reviewer",
  "arguments": {
    "metrics": {
      "weekly_review_priority_clarity": 80,
      "weekly_review_time_realism": 65,
      "weekly_review_next_action_named": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
