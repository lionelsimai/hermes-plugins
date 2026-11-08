---
name: memory-stale-memory-curator
description: "Stale Memory Curator for Hermes Agent: apply a checklist workflow to stale memory work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Stale Memory Curator

Use this skill in Hermes Agent when the task involves memory stale memory curator. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: stale memory fact accuracy, stale memory size budget fit, stale memory staleness.
2. Run the `memory_stale_memory_curator` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: stale memory duplication, stale memory source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
