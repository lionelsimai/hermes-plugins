# Slack Update Drafter

Slack Update Drafter for Hermes Agent: apply a score workflow to slack update work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_slack_update_drafter` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_slack_update_drafter",
  "arguments": {
    "metrics": {
      "slack_update_audience_fit": 80,
      "slack_update_tone_fit": 65,
      "slack_update_length_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
