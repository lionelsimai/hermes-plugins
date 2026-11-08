---
name: api-sync-job-spec-mapper
description: "Sync Job Spec Mapper for Hermes Agent: apply a classify workflow to sync job spec work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Sync Job Spec Mapper

Use this skill in Hermes Agent when the task involves api sync job spec mapper. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: sync job spec contract fit, sync job spec auth handled safely, sync job spec error cases covered.
2. Run the `api_sync_job_spec_mapper` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: sync job spec rate limits respected, sync job spec verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
