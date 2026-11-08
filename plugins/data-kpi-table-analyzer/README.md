# Kpi Table Analyzer

Kpi Table Analyzer for Hermes Agent: apply a score workflow to kpi table work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_kpi_table_analyzer` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_kpi_table_analyzer",
  "arguments": {
    "metrics": {
      "kpi_table_data_completeness": 80,
      "kpi_table_column_consistency": 65,
      "kpi_table_outliers_flagged": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
