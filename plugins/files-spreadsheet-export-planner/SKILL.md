---
name: files-spreadsheet-export-planner
description: "Spreadsheet Export Planner for Hermes Agent: apply a template workflow to spreadsheet export work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Spreadsheet Export Planner

Use this skill in Hermes Agent when the task involves files spreadsheet export planner. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: spreadsheet export format fit, spreadsheet export completeness, spreadsheet export naming consistency.
2. Run the `files_spreadsheet_export_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: spreadsheet export source fidelity, spreadsheet export output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
