---
name: files-text-extraction-summarizer
description: "Text Extraction Summarizer for Hermes Agent: apply a template workflow to text extraction work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Text Extraction Summarizer

Use this skill in Hermes Agent when the task involves files text extraction summarizer. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: text extraction format fit, text extraction completeness, text extraction naming consistency.
2. Run the `files_text_extraction_summarizer` tool (or follow this procedure manually) — kind: template.
3. Check the output against: text extraction source fidelity, text extraction output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
