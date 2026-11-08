---
name: files-markdown-note-planner
description: "Markdown Note Planner for Hermes Agent: apply a prioritize workflow to markdown note work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Markdown Note Planner

Use this skill in Hermes Agent when the task involves files markdown note planner. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: markdown note format fit, markdown note completeness, markdown note naming consistency.
2. Run the `files_markdown_note_planner` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: markdown note source fidelity, markdown note output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
