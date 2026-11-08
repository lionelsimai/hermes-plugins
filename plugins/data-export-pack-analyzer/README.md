# Export Pack Analyzer

Export Pack Analyzer for Hermes Agent: apply a prioritize workflow to export pack work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_export_pack_analyzer` (kind: prioritize)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_export_pack_analyzer",
  "arguments": {
    "items": [
      {
        "name": "Sample task A",
        "impact": 8,
        "effort": 3
      },
      {
        "name": "Sample task B",
        "impact": 6,
        "effort": 1
      }
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
