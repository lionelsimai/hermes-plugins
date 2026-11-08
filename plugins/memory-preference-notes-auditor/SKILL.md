---
name: memory-preference-notes-auditor
description: "Preference Notes Auditor for Hermes Agent: apply a checklist workflow to preference notes work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Preference Notes Auditor

Use this skill in Hermes Agent when the task involves memory preference notes auditor. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: preference notes fact accuracy, preference notes size budget fit, preference notes staleness.
2. Run the `memory_preference_notes_auditor` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: preference notes duplication, preference notes source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
