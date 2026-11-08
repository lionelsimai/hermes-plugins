# Site Navigation Checker

Site Navigation Checker for Hermes Agent: apply a analyze workflow to site navigation work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_site_navigation_checker` (kind: analyze)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_site_navigation_checker",
  "arguments": {
    "counts": {
      "site_navigation_step_clarity": 40,
      "site_navigation_fallback_step": 25,
      "site_navigation_data_accuracy": 10,
      "site_navigation_confirmation_gate": 75
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
