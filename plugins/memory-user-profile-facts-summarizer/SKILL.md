---
name: memory-user-profile-facts-summarizer
description: "User Profile Facts Summarizer for Hermes Agent: apply a score workflow to user profile facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# User Profile Facts Summarizer

Use this skill in Hermes Agent when the task involves memory user profile facts summarizer. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: user profile facts fact accuracy, user profile facts size budget fit, user profile facts staleness.
2. Run the `memory_user_profile_facts_summarizer` tool (or follow this procedure manually) — kind: score.
3. Check the output against: user profile facts duplication, user profile facts source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
