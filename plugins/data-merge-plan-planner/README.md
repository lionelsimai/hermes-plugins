# Merge Plan Planner

Merge Plan Planner for Hermes Agent: apply a score workflow to merge plan work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_merge_plan_planner` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_merge_plan_planner",
  "arguments": {
    "metrics": {
      "merge_plan_data_completeness": 80,
      "merge_plan_column_consistency": 65,
      "merge_plan_outliers_flagged": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
