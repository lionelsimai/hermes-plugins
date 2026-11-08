# Data Quality Check Cleaner

Data Quality Check Cleaner for Hermes Agent: apply a score workflow to data quality check work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_data_quality_check_cleaner` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_data_quality_check_cleaner",
  "arguments": {
    "metrics": {
      "data_quality_check_data_completeness": 80,
      "data_quality_check_column_consistency": 65,
      "data_quality_check_outliers_flagged": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
