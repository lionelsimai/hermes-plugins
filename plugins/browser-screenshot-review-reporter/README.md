# Screenshot Review Reporter

Screenshot Review Reporter for Hermes Agent: apply a score workflow to screenshot review work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_screenshot_review_reporter` (kind: score)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_screenshot_review_reporter",
  "arguments": {
    "metrics": {
      "screenshot_review_step_clarity": 80,
      "screenshot_review_fallback_step": 65,
      "screenshot_review_data_accuracy": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
