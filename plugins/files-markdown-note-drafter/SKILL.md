---
name: files-markdown-note-drafter
description: "Markdown Note Drafter for Hermes Agent: apply a plan workflow to markdown note work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Markdown Note Drafter

Use this skill in Hermes Agent when the task involves files markdown note drafter. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: markdown note format fit, markdown note completeness, markdown note naming consistency.
2. Run the `files_markdown_note_drafter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: markdown note source fidelity, markdown note output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
