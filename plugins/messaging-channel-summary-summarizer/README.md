# Channel Summary Summarizer

Channel Summary Summarizer for Hermes Agent: apply a analyze workflow to channel summary work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_channel_summary_summarizer` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_channel_summary_summarizer",
  "arguments": {
    "counts": {
      "channel_summary_audience_fit": 40,
      "channel_summary_tone_fit": 25,
      "channel_summary_length_fit": 10,
      "channel_summary_approval_gate": 75
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
