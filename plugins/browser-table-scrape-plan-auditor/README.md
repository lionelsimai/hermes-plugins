# Table Scrape Plan Auditor

Table Scrape Plan Auditor for Hermes Agent: apply a score workflow to table scrape plan work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_table_scrape_plan_auditor` (kind: score)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_table_scrape_plan_auditor",
  "arguments": {
    "metrics": {
      "table_scrape_plan_step_clarity": 80,
      "table_scrape_plan_fallback_step": 65,
      "table_scrape_plan_data_accuracy": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
