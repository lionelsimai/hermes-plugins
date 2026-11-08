---
name: core-skill-review-checklist
description: "Skill Review Checklist for Hermes Agent: apply a checklist workflow to skill review work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Skill Review Checklist

Use this skill in Hermes Agent when the task involves core skill review checklist. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: skill review goal clarity, skill review setup completeness, skill review toolset fit.
2. Run the `core_skill_review_checklist` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: skill review guardrail coverage, skill review verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
