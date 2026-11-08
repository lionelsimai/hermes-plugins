---
name: files-document-outline-summarizer
description: "Document Outline Summarizer for Hermes Agent: apply a analyze workflow to document outline work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Document Outline Summarizer

Use this skill in Hermes Agent when the task involves files document outline summarizer. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: document outline format fit, document outline completeness, document outline naming consistency.
2. Run the `files_document_outline_summarizer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: document outline source fidelity, document outline output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
