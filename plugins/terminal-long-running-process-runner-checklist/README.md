# Long Running Process Runner Checklist

Long Running Process Runner Checklist for Hermes Agent: apply a score workflow to long running process work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_long_running_process_runner_checklist` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_long_running_process_runner_checklist",
  "arguments": {
    "metrics": {
      "long_running_process_command_safety": 80,
      "long_running_process_expected_output": 65,
      "long_running_process_timeout_set": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
