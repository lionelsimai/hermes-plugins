# Inbox Triage Planner

Inbox Triage Planner for Hermes Agent: apply a analyze workflow to inbox triage work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_inbox_triage_planner` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_inbox_triage_planner",
  "arguments": {
    "counts": {
      "inbox_triage_priority_accuracy": 40,
      "inbox_triage_tone_fit": 25,
      "inbox_triage_facts_supplied_only": 10,
      "inbox_triage_approval_gate": 75
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
