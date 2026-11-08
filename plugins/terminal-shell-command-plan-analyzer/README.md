# Shell Command Plan Analyzer

Shell Command Plan Analyzer for Hermes Agent: apply a classify workflow to shell command plan work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_shell_command_plan_analyzer` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_shell_command_plan_analyzer",
  "arguments": {
    "text": "Please review: this concerns shell command plan command safety and shell command plan timeout set."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
