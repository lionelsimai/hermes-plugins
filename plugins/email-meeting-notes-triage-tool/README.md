# Meeting Notes Triage Tool

Meeting Notes Triage Tool for Hermes Agent: apply a analyze workflow to meeting notes work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_meeting_notes_triage_tool` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_meeting_notes_triage_tool",
  "arguments": {
    "counts": {
      "meeting_notes_priority_accuracy": 40,
      "meeting_notes_tone_fit": 25,
      "meeting_notes_facts_supplied_only": 10,
      "meeting_notes_approval_gate": 75
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
