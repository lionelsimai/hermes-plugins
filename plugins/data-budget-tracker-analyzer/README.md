# Budget Tracker Analyzer

Budget Tracker Analyzer for Hermes Agent: apply a analyze workflow to budget tracker work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_budget_tracker_analyzer` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_budget_tracker_analyzer",
  "arguments": {
    "counts": {
      "budget_tracker_data_completeness": 40,
      "budget_tracker_column_consistency": 25,
      "budget_tracker_outliers_flagged": 10,
      "budget_tracker_totals_verified": 75
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
