# Dashboard Check Reporter

Dashboard Check Reporter for Hermes Agent: apply a classify workflow to dashboard check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_dashboard_check_reporter` (kind: classify)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_dashboard_check_reporter",
  "arguments": {
    "text": "Please review: this concerns dashboard check step clarity and dashboard check data accuracy."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
