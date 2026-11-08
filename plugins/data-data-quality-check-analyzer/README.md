# Data Quality Check Analyzer

Data Quality Check Analyzer for Hermes Agent: apply a checklist workflow to data quality check work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_data_quality_check_analyzer` (kind: checklist)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_data_quality_check_analyzer",
  "arguments": {
    "completed": [
      "data quality check data completeness",
      "data quality check column consistency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
