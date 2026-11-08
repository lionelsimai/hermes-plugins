---
name: cron-sync-job-reporter
description: "Sync Job Reporter for Hermes Agent: apply a plan workflow to sync job work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Sync Job Reporter

Use this skill in Hermes Agent when the task involves cron sync job reporter. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: sync job schedule clarity, sync job delivery target, sync job failure handling.
2. Run the `cron_sync_job_reporter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: sync job idempotency, sync job owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
