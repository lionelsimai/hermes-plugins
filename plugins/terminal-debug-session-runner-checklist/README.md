# Debug Session Runner Checklist

Debug Session Runner Checklist for Hermes Agent: apply a score workflow to debug session work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_debug_session_runner_checklist` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_debug_session_runner_checklist",
  "arguments": {
    "metrics": {
      "debug_session_command_safety": 80,
      "debug_session_expected_output": 65,
      "debug_session_timeout_set": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
