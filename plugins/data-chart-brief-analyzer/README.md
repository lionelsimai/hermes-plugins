# Chart Brief Analyzer

Chart Brief Analyzer for Hermes Agent: apply a classify workflow to chart brief work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_chart_brief_analyzer` (kind: classify)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_chart_brief_analyzer",
  "arguments": {
    "text": "Please review: this concerns chart brief data completeness and chart brief outliers flagged."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
