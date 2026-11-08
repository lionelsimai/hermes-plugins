# Environment Setup Planner

Environment Setup Planner for Hermes Agent: apply a analyze workflow to environment setup work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_environment_setup_planner` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_environment_setup_planner",
  "arguments": {
    "counts": {
      "environment_setup_command_safety": 40,
      "environment_setup_expected_output": 25,
      "environment_setup_timeout_set": 10,
      "environment_setup_rollback_step": 75
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
