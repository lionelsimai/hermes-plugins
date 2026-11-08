---
name: core-onboarding-flow-checklist
description: "Onboarding Flow Checklist for Hermes Agent: apply a score workflow to onboarding flow work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Onboarding Flow Checklist

Use this skill in Hermes Agent when the task involves core onboarding flow checklist. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: onboarding flow goal clarity, onboarding flow setup completeness, onboarding flow toolset fit.
2. Run the `core_onboarding_flow_checklist` tool (or follow this procedure manually) — kind: score.
3. Check the output against: onboarding flow guardrail coverage, onboarding flow verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
