# File Rename Plan Drafter

File Rename Plan Drafter for Hermes Agent: apply a template workflow to file rename plan work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_file_rename_plan_drafter` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_file_rename_plan_drafter",
  "arguments": {
    "facts": {
      "file_rename_plan_format_fit": "Sample supplied fact",
      "file_rename_plan_completeness": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
