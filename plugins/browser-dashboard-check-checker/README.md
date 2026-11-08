# Dashboard Check Checker

Dashboard Check Checker for Hermes Agent: apply a checklist workflow to dashboard check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_dashboard_check_checker` (kind: checklist)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_dashboard_check_checker",
  "arguments": {
    "completed": [
      "dashboard check step clarity",
      "dashboard check fallback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
