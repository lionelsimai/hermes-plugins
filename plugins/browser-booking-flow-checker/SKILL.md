---
name: browser-booking-flow-checker
description: "Booking Flow Checker for Hermes Agent: apply a classify workflow to booking flow work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Booking Flow Checker

Use this skill in Hermes Agent when the task involves browser booking flow checker. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: booking flow step clarity, booking flow fallback step, booking flow data accuracy.
2. Run the `browser_booking_flow_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: booking flow confirmation gate, booking flow completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
