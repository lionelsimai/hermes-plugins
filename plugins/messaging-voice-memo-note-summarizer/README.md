# Voice Memo Note Summarizer

Voice Memo Note Summarizer for Hermes Agent: apply a score workflow to voice memo note work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_voice_memo_note_summarizer` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_voice_memo_note_summarizer",
  "arguments": {
    "metrics": {
      "voice_memo_note_audience_fit": 80,
      "voice_memo_note_tone_fit": 65,
      "voice_memo_note_length_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
