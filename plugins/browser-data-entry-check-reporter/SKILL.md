---
name: browser-data-entry-check-reporter
description: "Data Entry Check Reporter for Hermes Agent: apply a analyze workflow to data entry check work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Data Entry Check Reporter

Use this skill in Hermes Agent when the task involves browser data entry check reporter. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: data entry check step clarity, data entry check fallback step, data entry check data accuracy.
2. Run the `browser_data_entry_check_reporter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: data entry check confirmation gate, data entry check completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
