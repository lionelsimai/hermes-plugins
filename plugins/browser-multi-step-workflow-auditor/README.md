# Multi Step Workflow Auditor

Multi Step Workflow Auditor for Hermes Agent: apply a classify workflow to multi step workflow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_multi_step_workflow_auditor` (kind: classify)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_multi_step_workflow_auditor",
  "arguments": {
    "text": "Please review: this concerns multi step workflow step clarity and multi step workflow data accuracy."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
