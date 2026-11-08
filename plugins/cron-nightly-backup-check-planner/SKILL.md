---
name: cron-nightly-backup-check-planner
description: "Nightly Backup Check Planner for Hermes Agent: apply a classify workflow to nightly backup check work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Nightly Backup Check Planner

Use this skill in Hermes Agent when the task involves cron nightly backup check planner. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: nightly backup check schedule clarity, nightly backup check delivery target, nightly backup check failure handling.
2. Run the `cron_nightly_backup_check_planner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: nightly backup check idempotency, nightly backup check owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
