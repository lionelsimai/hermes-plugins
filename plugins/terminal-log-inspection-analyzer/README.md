# Log Inspection Analyzer

Log Inspection Analyzer for Hermes Agent: apply a score workflow to log inspection work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_log_inspection_analyzer` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_log_inspection_analyzer",
  "arguments": {
    "metrics": {
      "log_inspection_command_safety": 80,
      "log_inspection_expected_output": 65,
      "log_inspection_timeout_set": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
