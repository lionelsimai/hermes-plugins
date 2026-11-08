# File Rename Plan Planner

File Rename Plan Planner for Hermes Agent: apply a analyze workflow to file rename plan work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_file_rename_plan_planner` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_file_rename_plan_planner",
  "arguments": {
    "counts": {
      "file_rename_plan_format_fit": 40,
      "file_rename_plan_completeness": 25,
      "file_rename_plan_naming_consistency": 10,
      "file_rename_plan_source_fidelity": 75
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
