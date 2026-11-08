---
name: cron-job-failure-review-scheduler-review
description: "Job Failure Review Scheduler Review for Hermes Agent: apply a prioritize workflow to job failure review work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Job Failure Review Scheduler Review

Use this skill in Hermes Agent when the task involves cron job failure review scheduler review. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: job failure review schedule clarity, job failure review delivery target, job failure review failure handling.
2. Run the `cron_job_failure_review_scheduler_review` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: job failure review idempotency, job failure review owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
