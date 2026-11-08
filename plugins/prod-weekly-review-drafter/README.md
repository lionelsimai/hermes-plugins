# Weekly Review Drafter

Weekly Review Drafter for Hermes Agent: apply a template workflow to weekly review work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_weekly_review_drafter` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_weekly_review_drafter",
  "arguments": {
    "facts": {
      "weekly_review_priority_clarity": "Sample supplied fact",
      "weekly_review_time_realism": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
