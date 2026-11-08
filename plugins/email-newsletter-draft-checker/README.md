# Newsletter Draft Checker

Newsletter Draft Checker for Hermes Agent: apply a analyze workflow to newsletter draft work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_newsletter_draft_checker` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_newsletter_draft_checker",
  "arguments": {
    "counts": {
      "newsletter_draft_priority_accuracy": 40,
      "newsletter_draft_tone_fit": 25,
      "newsletter_draft_facts_supplied_only": 10,
      "newsletter_draft_approval_gate": 75
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
