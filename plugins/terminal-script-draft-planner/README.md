# Script Draft Planner

Script Draft Planner for Hermes Agent: apply a score workflow to script draft work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_script_draft_planner` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_script_draft_planner",
  "arguments": {
    "metrics": {
      "script_draft_command_safety": 80,
      "script_draft_expected_output": 65,
      "script_draft_timeout_set": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
