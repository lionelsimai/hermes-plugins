---
name: cron-reminder-job-planner
description: "Reminder Job Planner for Hermes Agent: apply a plan workflow to reminder job work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Reminder Job Planner

Use this skill in Hermes Agent when the task involves cron reminder job planner. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: reminder job schedule clarity, reminder job delivery target, reminder job failure handling.
2. Run the `cron_reminder_job_planner` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: reminder job idempotency, reminder job owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
