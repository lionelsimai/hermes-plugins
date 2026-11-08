---
name: browser-screenshot-review-reporter
description: "Screenshot Review Reporter for Hermes Agent: apply a score workflow to screenshot review work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Screenshot Review Reporter

Use this skill in Hermes Agent when the task involves browser screenshot review reporter. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: screenshot review step clarity, screenshot review fallback step, screenshot review data accuracy.
2. Run the `browser_screenshot_review_reporter` tool (or follow this procedure manually) — kind: score.
3. Check the output against: screenshot review confirmation gate, screenshot review completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
