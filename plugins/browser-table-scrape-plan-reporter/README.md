# Table Scrape Plan Reporter

Table Scrape Plan Reporter for Hermes Agent: apply a template workflow to table scrape plan work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_table_scrape_plan_reporter` (kind: template)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_table_scrape_plan_reporter",
  "arguments": {
    "facts": {
      "table_scrape_plan_step_clarity": "Sample supplied fact",
      "table_scrape_plan_fallback_step": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
