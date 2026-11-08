# Table Cleanup Checker

Table Cleanup Checker for Hermes Agent: apply a analyze workflow to table cleanup work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_table_cleanup_checker` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_table_cleanup_checker",
  "arguments": {
    "counts": {
      "table_cleanup_data_completeness": 40,
      "table_cleanup_column_consistency": 25,
      "table_cleanup_outliers_flagged": 10,
      "table_cleanup_totals_verified": 75
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
