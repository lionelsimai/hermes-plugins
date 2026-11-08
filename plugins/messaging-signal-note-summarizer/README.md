# Signal Note Summarizer

Signal Note Summarizer for Hermes Agent: apply a classify workflow to signal note work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_signal_note_summarizer` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_signal_note_summarizer",
  "arguments": {
    "text": "Please review: this concerns signal note audience fit and signal note length fit."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
