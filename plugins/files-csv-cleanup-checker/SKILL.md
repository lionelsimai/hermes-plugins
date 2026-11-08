---
name: files-csv-cleanup-checker
description: "Csv Cleanup Checker for Hermes Agent: apply a template workflow to csv cleanup work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Csv Cleanup Checker

Use this skill in Hermes Agent when the task involves files csv cleanup checker. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: csv cleanup format fit, csv cleanup completeness, csv cleanup naming consistency.
2. Run the `files_csv_cleanup_checker` tool (or follow this procedure manually) — kind: template.
3. Check the output against: csv cleanup source fidelity, csv cleanup output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
