# Channel Summary Triage Tool

Channel Summary Triage Tool for Hermes Agent: apply a template workflow to channel summary work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_channel_summary_triage_tool` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_channel_summary_triage_tool",
  "arguments": {
    "facts": {
      "channel_summary_audience_fit": "Sample supplied fact",
      "channel_summary_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
