---
name: community-health-report-drafter
description: "Health Report Drafter for Hermes Agent: apply a prioritize workflow to health report work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Health Report Drafter

Use this skill in Hermes Agent when the task involves community health report drafter. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: health report member fit, health report tone fit, health report approval gate.
2. Run the `community_health_report_drafter` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: health report safety check, health report follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
