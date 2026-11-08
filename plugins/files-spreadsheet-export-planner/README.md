# Spreadsheet Export Planner

Spreadsheet Export Planner for Hermes Agent: apply a template workflow to spreadsheet export work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_spreadsheet_export_planner` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_spreadsheet_export_planner",
  "arguments": {
    "facts": {
      "spreadsheet_export_format_fit": "Sample supplied fact",
      "spreadsheet_export_completeness": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
