# Table Cleanup Analyzer

Table Cleanup Analyzer for Hermes Agent: apply a template workflow to table cleanup work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_table_cleanup_analyzer` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_table_cleanup_analyzer",
  "arguments": {
    "facts": {
      "table_cleanup_data_completeness": "Sample supplied fact",
      "table_cleanup_column_consistency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
