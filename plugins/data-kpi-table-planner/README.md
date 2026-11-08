# Kpi Table Planner

Kpi Table Planner for Hermes Agent: apply a analyze workflow to kpi table work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_kpi_table_planner` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_kpi_table_planner",
  "arguments": {
    "counts": {
      "kpi_table_data_completeness": 40,
      "kpi_table_column_consistency": 25,
      "kpi_table_outliers_flagged": 10,
      "kpi_table_totals_verified": 75
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
