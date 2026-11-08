# Ssh Task Auditor

Ssh Task Auditor for Hermes Agent: apply a score workflow to ssh task work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_ssh_task_auditor` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_ssh_task_auditor",
  "arguments": {
    "metrics": {
      "ssh_task_command_safety": 80,
      "ssh_task_expected_output": 65,
      "ssh_task_timeout_set": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
