# Slack Update Summarizer

Slack Update Summarizer for Hermes Agent: apply a template workflow to slack update work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_slack_update_summarizer` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_slack_update_summarizer",
  "arguments": {
    "facts": {
      "slack_update_audience_fit": "Sample supplied fact",
      "slack_update_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
