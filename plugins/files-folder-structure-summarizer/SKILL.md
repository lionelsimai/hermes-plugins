---
name: files-folder-structure-summarizer
description: "Folder Structure Summarizer for Hermes Agent: apply a audit workflow to folder structure work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Folder Structure Summarizer

Use this skill in Hermes Agent when the task involves files folder structure summarizer. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: folder structure format fit, folder structure completeness, folder structure naming consistency.
2. Run the `files_folder_structure_summarizer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: folder structure source fidelity, folder structure output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
