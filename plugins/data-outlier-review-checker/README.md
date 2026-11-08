# Outlier Review Checker

Outlier Review Checker for Hermes Agent: apply a analyze workflow to outlier review work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_outlier_review_checker` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_outlier_review_checker",
  "arguments": {
    "counts": {
      "outlier_review_data_completeness": 40,
      "outlier_review_column_consistency": 25,
      "outlier_review_outliers_flagged": 10,
      "outlier_review_totals_verified": 75
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
