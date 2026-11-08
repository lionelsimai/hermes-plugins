# Multi Step Workflow Sequencer

Multi Step Workflow Sequencer for Hermes Agent: apply a audit workflow to multi step workflow work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_multi_step_workflow_sequencer` (kind: audit)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_multi_step_workflow_sequencer",
  "arguments": {
    "text": "This sample covers multi step workflow step clarity and multi step workflow fallback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
