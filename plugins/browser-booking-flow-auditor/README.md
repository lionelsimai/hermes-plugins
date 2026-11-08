# Booking Flow Auditor

Booking Flow Auditor for Hermes Agent: apply a audit workflow to booking flow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_booking_flow_auditor` (kind: audit)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_booking_flow_auditor",
  "arguments": {
    "text": "This sample covers booking flow step clarity and booking flow fallback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
