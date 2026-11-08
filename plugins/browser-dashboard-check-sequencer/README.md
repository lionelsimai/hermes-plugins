# Dashboard Check Sequencer

Dashboard Check Sequencer for Hermes Agent: apply a analyze workflow to dashboard check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_dashboard_check_sequencer` (kind: analyze)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_dashboard_check_sequencer",
  "arguments": {
    "counts": {
      "dashboard_check_step_clarity": 40,
      "dashboard_check_fallback_step": 25,
      "dashboard_check_data_accuracy": 10,
      "dashboard_check_confirmation_gate": 75
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
