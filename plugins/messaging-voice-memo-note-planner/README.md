# Voice Memo Note Planner

Voice Memo Note Planner for Hermes Agent: apply a template workflow to voice memo note work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_voice_memo_note_planner` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_voice_memo_note_planner",
  "arguments": {
    "facts": {
      "voice_memo_note_audience_fit": "Sample supplied fact",
      "voice_memo_note_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
