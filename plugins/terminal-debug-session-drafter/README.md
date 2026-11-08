# Debug Session Drafter

Debug Session Drafter for Hermes Agent: apply a analyze workflow to debug session work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_debug_session_drafter` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_debug_session_drafter",
  "arguments": {
    "counts": {
      "debug_session_command_safety": 40,
      "debug_session_expected_output": 25,
      "debug_session_timeout_set": 10,
      "debug_session_rollback_step": 75
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
