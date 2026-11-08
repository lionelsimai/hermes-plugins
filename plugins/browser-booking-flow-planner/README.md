# Booking Flow Planner

Booking Flow Planner for Hermes Agent: apply a analyze workflow to booking flow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_booking_flow_planner` (kind: analyze)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_booking_flow_planner",
  "arguments": {
    "counts": {
      "booking_flow_step_clarity": 40,
      "booking_flow_fallback_step": 25,
      "booking_flow_data_accuracy": 10,
      "booking_flow_confirmation_gate": 75
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
