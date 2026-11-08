---
name: community-feedback-summary-reporter
description: "Feedback Summary Reporter for Hermes Agent: apply a plan workflow to feedback summary work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Feedback Summary Reporter

Use this skill in Hermes Agent when the task involves community feedback summary reporter. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: feedback summary member fit, feedback summary tone fit, feedback summary approval gate.
2. Run the `community_feedback_summary_reporter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: feedback summary safety check, feedback summary follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
