# Log Inspection Drafter

Log Inspection Drafter for Hermes Agent: apply a template workflow to log inspection work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_log_inspection_drafter` (kind: template)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_log_inspection_drafter",
  "arguments": {
    "facts": {
      "log_inspection_command_safety": "Sample supplied fact",
      "log_inspection_expected_output": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
