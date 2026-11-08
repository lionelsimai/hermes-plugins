---
name: browser-site-navigation-sequencer
description: "Site Navigation Sequencer for Hermes Agent: apply a audit workflow to site navigation work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Site Navigation Sequencer

Use this skill in Hermes Agent when the task involves browser site navigation sequencer. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: site navigation step clarity, site navigation fallback step, site navigation data accuracy.
2. Run the `browser_site_navigation_sequencer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: site navigation confirmation gate, site navigation completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
