# Follow Up Note Summarizer

Follow Up Note Summarizer for Hermes Agent: apply a score workflow to follow up note work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_follow_up_note_summarizer` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_follow_up_note_summarizer",
  "arguments": {
    "metrics": {
      "follow_up_note_priority_accuracy": 80,
      "follow_up_note_tone_fit": 65,
      "follow_up_note_facts_supplied_only": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
