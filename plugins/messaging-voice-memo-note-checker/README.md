# Voice Memo Note Checker

Voice Memo Note Checker for Hermes Agent: apply a checklist workflow to voice memo note work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_voice_memo_note_checker` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_voice_memo_note_checker",
  "arguments": {
    "completed": [
      "voice memo note audience fit",
      "voice memo note tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
