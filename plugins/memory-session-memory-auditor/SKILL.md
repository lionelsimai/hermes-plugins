---
name: memory-session-memory-auditor
description: "Session Memory Auditor for Hermes Agent: apply a template workflow to session memory work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Session Memory Auditor

Use this skill in Hermes Agent when the task involves memory session memory auditor. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: session memory fact accuracy, session memory size budget fit, session memory staleness.
2. Run the `memory_session_memory_auditor` tool (or follow this procedure manually) — kind: template.
3. Check the output against: session memory duplication, session memory source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
