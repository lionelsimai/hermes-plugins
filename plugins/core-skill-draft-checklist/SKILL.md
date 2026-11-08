---
name: core-skill-draft-checklist
description: "Skill Draft Checklist for Hermes Agent: apply a classify workflow to skill draft work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Skill Draft Checklist

Use this skill in Hermes Agent when the task involves core skill draft checklist. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: skill draft goal clarity, skill draft setup completeness, skill draft toolset fit.
2. Run the `core_skill_draft_checklist` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: skill draft guardrail coverage, skill draft verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
