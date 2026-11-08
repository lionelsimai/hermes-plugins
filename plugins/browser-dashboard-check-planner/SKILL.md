---
name: browser-dashboard-check-planner
description: "Dashboard Check Planner for Hermes Agent: apply a score workflow to dashboard check work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Dashboard Check Planner

Use this skill in Hermes Agent when the task involves browser dashboard check planner. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: dashboard check step clarity, dashboard check fallback step, dashboard check data accuracy.
2. Run the `browser_dashboard_check_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: dashboard check confirmation gate, dashboard check completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
