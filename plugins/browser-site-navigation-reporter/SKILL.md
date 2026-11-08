---
name: browser-site-navigation-reporter
description: "Site Navigation Reporter for Hermes Agent: apply a plan workflow to site navigation work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Site Navigation Reporter

Use this skill in Hermes Agent when the task involves browser site navigation reporter. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: site navigation step clarity, site navigation fallback step, site navigation data accuracy.
2. Run the `browser_site_navigation_reporter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: site navigation confirmation gate, site navigation completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
