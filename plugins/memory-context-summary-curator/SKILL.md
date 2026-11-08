---
name: memory-context-summary-curator
description: "Context Summary Curator for Hermes Agent: apply a prioritize workflow to context summary work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Context Summary Curator

Use this skill in Hermes Agent when the task involves memory context summary curator. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: context summary fact accuracy, context summary size budget fit, context summary staleness.
2. Run the `memory_context_summary_curator` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: context summary duplication, context summary source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
