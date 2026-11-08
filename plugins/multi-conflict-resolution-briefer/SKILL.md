---
name: multi-conflict-resolution-briefer
description: "Conflict Resolution Briefer for Hermes Agent: apply a score workflow to conflict resolution work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Conflict Resolution Briefer

Use this skill in Hermes Agent when the task involves multi conflict resolution briefer. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: conflict resolution scope clarity, conflict resolution independence of subtasks, conflict resolution merge criteria.
2. Run the `multi_conflict_resolution_briefer` tool (or follow this procedure manually) — kind: score.
3. Check the output against: conflict resolution context budget, conflict resolution verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
