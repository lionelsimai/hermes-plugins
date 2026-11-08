# Shell Command Plan Auditor

Shell Command Plan Auditor for Hermes Agent: apply a audit workflow to shell command plan work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_shell_command_plan_auditor` (kind: audit)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_shell_command_plan_auditor",
  "arguments": {
    "text": "This sample covers shell command plan command safety and shell command plan expected output in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
