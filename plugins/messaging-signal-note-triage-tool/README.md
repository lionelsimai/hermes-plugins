# Signal Note Triage Tool

Signal Note Triage Tool for Hermes Agent: apply a analyze workflow to signal note work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_signal_note_triage_tool` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_signal_note_triage_tool",
  "arguments": {
    "counts": {
      "signal_note_audience_fit": 40,
      "signal_note_tone_fit": 25,
      "signal_note_length_fit": 10,
      "signal_note_approval_gate": 75
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
