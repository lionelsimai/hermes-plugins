# Travel Hold Summarizer

Travel Hold Summarizer for Hermes Agent: apply a classify workflow to travel hold work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_travel_hold_summarizer` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_travel_hold_summarizer",
  "arguments": {
    "text": "Please review: this concerns travel hold priority accuracy and travel hold facts supplied only."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
