# Slack Update Triage Tool

Slack Update Triage Tool for Hermes Agent: apply a checklist workflow to slack update work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_slack_update_triage_tool` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_slack_update_triage_tool",
  "arguments": {
    "completed": [
      "slack update audience fit",
      "slack update tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
