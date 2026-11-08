---
name: memory-session-memory-planner
description: "Session Memory Planner for Hermes Agent: apply a audit workflow to session memory work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Session Memory Planner

Use this skill in Hermes Agent when the task involves memory session memory planner. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: session memory fact accuracy, session memory size budget fit, session memory staleness.
2. Run the `memory_session_memory_planner` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: session memory duplication, session memory source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
