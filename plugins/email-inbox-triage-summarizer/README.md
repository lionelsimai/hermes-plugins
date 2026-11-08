# Inbox Triage Summarizer

Inbox Triage Summarizer for Hermes Agent: apply a classify workflow to inbox triage work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.

- Category: Email & Calendar
- Tool: `email_inbox_triage_summarizer` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "email_inbox_triage_summarizer",
  "arguments": {
    "text": "Please review: this concerns inbox triage priority accuracy and inbox triage facts supplied only."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
