# Inbox Triage Triage Tool

Inbox Triage Triage Tool for Hermes Agent: apply a score workflow to inbox triage work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_inbox_triage_triage_tool` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_inbox_triage_triage_tool",
  "arguments": {
    "metrics": {
      "inbox_triage_priority_accuracy": 80,
      "inbox_triage_tone_fit": 65,
      "inbox_triage_facts_supplied_only": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
