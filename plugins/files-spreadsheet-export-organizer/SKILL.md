---
name: files-spreadsheet-export-organizer
description: "Spreadsheet Export Organizer for Hermes Agent: apply a plan workflow to spreadsheet export work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Spreadsheet Export Organizer

Use this skill in Hermes Agent when the task involves files spreadsheet export organizer. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: spreadsheet export format fit, spreadsheet export completeness, spreadsheet export naming consistency.
2. Run the `files_spreadsheet_export_organizer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: spreadsheet export source fidelity, spreadsheet export output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
