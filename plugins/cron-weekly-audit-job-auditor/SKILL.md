---
name: cron-weekly-audit-job-auditor
description: "Weekly Audit Job Auditor for Hermes Agent: apply a template workflow to weekly audit job work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Weekly Audit Job Auditor

Use this skill in Hermes Agent when the task involves cron weekly audit job auditor. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: weekly audit job schedule clarity, weekly audit job delivery target, weekly audit job failure handling.
2. Run the `cron_weekly_audit_job_auditor` tool (or follow this procedure manually) — kind: template.
3. Check the output against: weekly audit job idempotency, weekly audit job owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
