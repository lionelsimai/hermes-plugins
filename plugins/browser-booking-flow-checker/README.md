# Booking Flow Checker

Booking Flow Checker for Hermes Agent: apply a classify workflow to booking flow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_booking_flow_checker` (kind: classify)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_booking_flow_checker",
  "arguments": {
    "text": "Please review: this concerns booking flow step clarity and booking flow data accuracy."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
