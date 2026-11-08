# Form Fill Plan Reporter

Form Fill Plan Reporter for Hermes Agent: apply a checklist workflow to form fill plan work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_form_fill_plan_reporter` (kind: checklist)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_form_fill_plan_reporter",
  "arguments": {
    "completed": [
      "form fill plan step clarity",
      "form fill plan fallback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
