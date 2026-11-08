# Script Draft Auditor

Script Draft Auditor for Hermes Agent: apply a analyze workflow to script draft work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_script_draft_auditor` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_script_draft_auditor",
  "arguments": {
    "counts": {
      "script_draft_command_safety": 40,
      "script_draft_expected_output": 25,
      "script_draft_timeout_set": 10,
      "script_draft_rollback_step": 75
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
