---
name: cron-job-failure-review-auditor
description: "Job Failure Review Auditor for Hermes Agent: apply a audit workflow to job failure review work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Job Failure Review Auditor

Use this skill in Hermes Agent when the task involves cron job failure review auditor. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: job failure review schedule clarity, job failure review delivery target, job failure review failure handling.
2. Run the `cron_job_failure_review_auditor` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: job failure review idempotency, job failure review owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
