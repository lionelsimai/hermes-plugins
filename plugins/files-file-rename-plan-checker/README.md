# File Rename Plan Checker

File Rename Plan Checker for Hermes Agent: apply a checklist workflow to file rename plan work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_file_rename_plan_checker` (kind: checklist)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_file_rename_plan_checker",
  "arguments": {
    "completed": [
      "file rename plan format fit",
      "file rename plan completeness"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
