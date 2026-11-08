---
name: cron-report-delivery-checker
description: "Report Delivery Checker for Hermes Agent: apply a checklist workflow to report delivery work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Report Delivery Checker

Use this skill in Hermes Agent when the task involves cron report delivery checker. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: report delivery schedule clarity, report delivery delivery target, report delivery failure handling.
2. Run the `cron_report_delivery_checker` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: report delivery idempotency, report delivery owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
