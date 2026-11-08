# Signal Note Checker

Signal Note Checker for Hermes Agent: apply a audit workflow to signal note work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_signal_note_checker` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_signal_note_checker",
  "arguments": {
    "text": "This sample covers signal note audience fit and signal note tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
