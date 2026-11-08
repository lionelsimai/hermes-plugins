# Docker Task Runner Checklist

Docker Task Runner Checklist for Hermes Agent: apply a analyze workflow to docker task work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_docker_task_runner_checklist` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_docker_task_runner_checklist",
  "arguments": {
    "counts": {
      "docker_task_command_safety": 40,
      "docker_task_expected_output": 25,
      "docker_task_timeout_set": 10,
      "docker_task_rollback_step": 75
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
