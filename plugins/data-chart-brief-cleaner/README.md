# Chart Brief Cleaner

Chart Brief Cleaner for Hermes Agent: apply a analyze workflow to chart brief work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_chart_brief_cleaner` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_chart_brief_cleaner",
  "arguments": {
    "counts": {
      "chart_brief_data_completeness": 40,
      "chart_brief_column_consistency": 25,
      "chart_brief_outliers_flagged": 10,
      "chart_brief_totals_verified": 75
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
