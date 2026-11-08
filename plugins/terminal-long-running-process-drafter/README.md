# Long Running Process Drafter

Long Running Process Drafter for Hermes Agent: apply a analyze workflow to long running process work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_long_running_process_drafter` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_long_running_process_drafter",
  "arguments": {
    "counts": {
      "long_running_process_command_safety": 40,
      "long_running_process_expected_output": 25,
      "long_running_process_timeout_set": 10,
      "long_running_process_rollback_step": 75
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
