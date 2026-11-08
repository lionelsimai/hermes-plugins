# Export Pack Planner

Export Pack Planner for Hermes Agent: apply a template workflow to export pack work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_export_pack_planner` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_export_pack_planner",
  "arguments": {
    "facts": {
      "export_pack_data_completeness": "Sample supplied fact",
      "export_pack_column_consistency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
