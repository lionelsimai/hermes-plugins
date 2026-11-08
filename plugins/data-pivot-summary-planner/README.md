# Pivot Summary Planner

Pivot Summary Planner for Hermes Agent: apply a template workflow to pivot summary work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_pivot_summary_planner` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_pivot_summary_planner",
  "arguments": {
    "facts": {
      "pivot_summary_data_completeness": "Sample supplied fact",
      "pivot_summary_column_consistency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
