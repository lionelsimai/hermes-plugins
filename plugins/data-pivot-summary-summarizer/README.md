# Pivot Summary Summarizer

Pivot Summary Summarizer for Hermes Agent: apply a checklist workflow to pivot summary work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_pivot_summary_summarizer` (kind: checklist)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_pivot_summary_summarizer",
  "arguments": {
    "completed": [
      "pivot summary data completeness",
      "pivot summary column consistency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
