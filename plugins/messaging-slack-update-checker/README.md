# Slack Update Checker

Slack Update Checker for Hermes Agent: apply a analyze workflow to slack update work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_slack_update_checker` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_slack_update_checker",
  "arguments": {
    "counts": {
      "slack_update_audience_fit": 40,
      "slack_update_tone_fit": 25,
      "slack_update_length_fit": 10,
      "slack_update_approval_gate": 75
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
