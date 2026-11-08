# Follow Up Note Triage Tool

Follow Up Note Triage Tool for Hermes Agent: apply a classify workflow to follow up note work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_follow_up_note_triage_tool` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_follow_up_note_triage_tool",
  "arguments": {
    "text": "Please review: this concerns follow up note priority accuracy and follow up note facts supplied only."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
