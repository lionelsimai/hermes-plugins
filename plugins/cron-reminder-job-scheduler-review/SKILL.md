---
name: cron-reminder-job-scheduler-review
description: "Reminder Job Scheduler Review for Hermes Agent: apply a checklist workflow to reminder job work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Reminder Job Scheduler Review

Use this skill in Hermes Agent when the task involves cron reminder job scheduler review. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: reminder job schedule clarity, reminder job delivery target, reminder job failure handling.
2. Run the `cron_reminder_job_scheduler_review` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: reminder job idempotency, reminder job owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
