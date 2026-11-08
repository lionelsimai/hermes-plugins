# Shell Command Plan Planner

Shell Command Plan Planner for Hermes Agent: apply a template workflow to shell command plan work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_shell_command_plan_planner` (kind: template)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_shell_command_plan_planner",
  "arguments": {
    "facts": {
      "shell_command_plan_command_safety": "Sample supplied fact",
      "shell_command_plan_expected_output": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
