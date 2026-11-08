---
name: cron-monitoring-job-reporter
description: "Monitoring Job Reporter for Hermes Agent: apply a prioritize workflow to monitoring job work — covers schedule clarity, delivery target and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Scheduling & Cron, Hermes, Plugins]
    category: scheduling-cron
---

# Monitoring Job Reporter

Use this skill in Hermes Agent when the task involves cron monitoring job reporter. It sits in the Scheduling & Cron category; the suggested Hermes toolset is `cron`.

## Workflow
1. Confirm the goal and gather supplied facts about: monitoring job schedule clarity, monitoring job delivery target, monitoring job failure handling.
2. Run the `cron_monitoring_job_reporter` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: monitoring job idempotency, monitoring job owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
