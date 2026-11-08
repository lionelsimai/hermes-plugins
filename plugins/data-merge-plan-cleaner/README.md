# Merge Plan Cleaner

Merge Plan Cleaner for Hermes Agent: apply a classify workflow to merge plan work — covers data completeness, column consistency and format fit, using supplied facts only.

- Category: Data & Spreadsheets
- Tool: `data_merge_plan_cleaner` (kind: classify)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "data_merge_plan_cleaner",
  "arguments": {
    "text": "Please review: this concerns merge plan data completeness and merge plan outliers flagged."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
