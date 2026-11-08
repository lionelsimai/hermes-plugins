---
name: core-profile-migration-checklist
description: "Profile Migration Checklist for Hermes Agent: apply a analyze workflow to profile migration work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Profile Migration Checklist

Use this skill in Hermes Agent when the task involves core profile migration checklist. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: profile migration goal clarity, profile migration setup completeness, profile migration toolset fit.
2. Run the `core_profile_migration_checklist` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: profile migration guardrail coverage, profile migration verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
