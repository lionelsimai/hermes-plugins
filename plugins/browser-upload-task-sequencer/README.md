# Upload Task Sequencer

Upload Task Sequencer for Hermes Agent: apply a score workflow to upload task work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_upload_task_sequencer` (kind: score)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_upload_task_sequencer",
  "arguments": {
    "metrics": {
      "upload_task_step_clarity": 80,
      "upload_task_fallback_step": 65,
      "upload_task_data_accuracy": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
