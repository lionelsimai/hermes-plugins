---
name: browser-table-scrape-plan-reporter
description: "Table Scrape Plan Reporter for Hermes Agent: apply a template workflow to table scrape plan work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Table Scrape Plan Reporter

Use this skill in Hermes Agent when the task involves browser table scrape plan reporter. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: table scrape plan step clarity, table scrape plan fallback step, table scrape plan data accuracy.
2. Run the `browser_table_scrape_plan_reporter` tool (or follow this procedure manually) — kind: template.
3. Check the output against: table scrape plan confirmation gate, table scrape plan completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
