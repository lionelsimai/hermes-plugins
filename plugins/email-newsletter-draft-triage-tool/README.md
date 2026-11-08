# Newsletter Draft Triage Tool

Newsletter Draft Triage Tool for Hermes Agent: apply a checklist workflow to newsletter draft work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_newsletter_draft_triage_tool` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_newsletter_draft_triage_tool",
  "arguments": {
    "completed": [
      "newsletter draft priority accuracy",
      "newsletter draft tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
