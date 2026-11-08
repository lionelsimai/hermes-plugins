# Form Fill Plan Sequencer

Form Fill Plan Sequencer for Hermes Agent: apply a score workflow to form fill plan work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_form_fill_plan_sequencer` (kind: score)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_form_fill_plan_sequencer",
  "arguments": {
    "metrics": {
      "form_fill_plan_step_clarity": 80,
      "form_fill_plan_fallback_step": 65,
      "form_fill_plan_data_accuracy": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
