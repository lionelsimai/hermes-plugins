# Table Scrape Plan Sequencer

Table Scrape Plan Sequencer for Hermes Agent: apply a checklist workflow to table scrape plan work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_table_scrape_plan_sequencer` (kind: checklist)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_table_scrape_plan_sequencer",
  "arguments": {
    "completed": [
      "table scrape plan step clarity",
      "table scrape plan fallback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
