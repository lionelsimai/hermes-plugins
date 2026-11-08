---
name: memory-session-recall-auditor
description: "Session Recall Auditor for Hermes Agent: apply a prioritize workflow to session recall work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Session Recall Auditor

Use this skill in Hermes Agent when the task involves memory session recall auditor. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: session recall fact accuracy, session recall size budget fit, session recall staleness.
2. Run the `memory_session_recall_auditor` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: session recall duplication, session recall source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
