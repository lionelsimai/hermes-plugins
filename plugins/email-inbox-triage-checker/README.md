# Inbox Triage Checker

Inbox Triage Checker for Hermes Agent: apply a template workflow to inbox triage work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_inbox_triage_checker` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_inbox_triage_checker",
  "arguments": {
    "facts": {
      "inbox_triage_priority_accuracy": "Sample supplied fact",
      "inbox_triage_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
