# Multi Step Workflow Planner

Multi Step Workflow Planner for Hermes Agent: apply a template workflow to multi step workflow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_multi_step_workflow_planner` (kind: template)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_multi_step_workflow_planner",
  "arguments": {
    "facts": {
      "multi_step_workflow_step_clarity": "Sample supplied fact",
      "multi_step_workflow_fallback_step": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
