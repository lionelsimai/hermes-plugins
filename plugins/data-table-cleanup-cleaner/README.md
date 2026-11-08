# Table Cleanup Cleaner

Table Cleanup Cleaner for Hermes Agent: apply a checklist workflow to table cleanup work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_table_cleanup_cleaner` (kind: checklist)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_table_cleanup_cleaner",
  "arguments": {
    "completed": [
      "table cleanup data completeness",
      "table cleanup column consistency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
