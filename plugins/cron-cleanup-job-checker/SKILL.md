---
name: cron-cleanup-job-checker
description: "Cleanup Job Checker for Hermes Agent: apply a prioritize workflow to cleanup job work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Cleanup Job Checker

Use this skill in Hermes Agent when the task involves cron cleanup job checker. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: cleanup job schedule clarity, cleanup job delivery target, cleanup job failure handling.
2. Run the `cron_cleanup_job_checker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: cleanup job idempotency, cleanup job owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
