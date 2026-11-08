# Survey Results Summarizer

Survey Results Summarizer for Hermes Agent: apply a score workflow to survey results work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_survey_results_summarizer` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_survey_results_summarizer",
  "arguments": {
    "metrics": {
      "survey_results_data_completeness": 80,
      "survey_results_column_consistency": 65,
      "survey_results_outliers_flagged": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
