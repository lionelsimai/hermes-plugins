# Upload Task Planner

Upload Task Planner for Hermes Agent: apply a audit workflow to upload task work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_upload_task_planner` (kind: audit)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_upload_task_planner",
  "arguments": {
    "text": "This sample covers upload task step clarity and upload task fallback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
