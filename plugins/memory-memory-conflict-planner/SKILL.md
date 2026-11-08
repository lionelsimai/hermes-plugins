---
name: memory-memory-conflict-planner
description: "Memory Conflict Planner for Hermes Agent: apply a score workflow to memory conflict work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Memory Conflict Planner

Use this skill in Hermes Agent when the task involves memory memory conflict planner. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: memory conflict fact accuracy, memory conflict size budget fit, memory conflict staleness.
2. Run the `memory_memory_conflict_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: memory conflict duplication, memory conflict source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
