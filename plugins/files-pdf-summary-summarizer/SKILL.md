---
name: files-pdf-summary-summarizer
description: "Pdf Summary Summarizer for Hermes Agent: apply a plan workflow to pdf summary work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Pdf Summary Summarizer

Use this skill in Hermes Agent when the task involves files pdf summary summarizer. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: pdf summary format fit, pdf summary completeness, pdf summary naming consistency.
2. Run the `files_pdf_summary_summarizer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: pdf summary source fidelity, pdf summary output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
