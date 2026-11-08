---
name: memory-project-facts-summarizer
description: "Project Facts Summarizer for Hermes Agent: apply a audit workflow to project facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Project Facts Summarizer

Use this skill in Hermes Agent when the task involves memory project facts summarizer. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: project facts fact accuracy, project facts size budget fit, project facts staleness.
2. Run the `memory_project_facts_summarizer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: project facts duplication, project facts source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
