# Reply Draft Planner

Reply Draft Planner for Hermes Agent: apply a score workflow to reply draft work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_reply_draft_planner` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_reply_draft_planner",
  "arguments": {
    "metrics": {
      "reply_draft_priority_accuracy": 80,
      "reply_draft_tone_fit": 65,
      "reply_draft_facts_supplied_only": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
