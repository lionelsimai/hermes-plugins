# Kpi Table Checker

Kpi Table Checker for Hermes Agent: apply a checklist workflow to kpi table work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_kpi_table_checker` (kind: checklist)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_kpi_table_checker",
  "arguments": {
    "completed": [
      "kpi table data completeness",
      "kpi table column consistency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
