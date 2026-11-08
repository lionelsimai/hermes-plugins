---
name: cron-report-delivery-reporter
description: "Report Delivery Reporter for Hermes Agent: apply a analyze workflow to report delivery work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Report Delivery Reporter

Use this skill in Hermes Agent when the task involves cron report delivery reporter. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: report delivery schedule clarity, report delivery delivery target, report delivery failure handling.
2. Run the `cron_report_delivery_reporter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: report delivery idempotency, report delivery owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
