# Multi Step Workflow Checker

Multi Step Workflow Checker for Hermes Agent: apply a analyze workflow to multi step workflow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_multi_step_workflow_checker` (kind: analyze)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_multi_step_workflow_checker",
  "arguments": {
    "counts": {
      "multi_step_workflow_step_clarity": 40,
      "multi_step_workflow_fallback_step": 25,
      "multi_step_workflow_data_accuracy": 10,
      "multi_step_workflow_confirmation_gate": 75
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
