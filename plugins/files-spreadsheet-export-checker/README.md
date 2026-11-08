# Spreadsheet Export Checker

Spreadsheet Export Checker for Hermes Agent: apply a score workflow to spreadsheet export work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_spreadsheet_export_checker` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_spreadsheet_export_checker",
  "arguments": {
    "metrics": {
      "spreadsheet_export_format_fit": 80,
      "spreadsheet_export_completeness": 65,
      "spreadsheet_export_naming_consistency": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
