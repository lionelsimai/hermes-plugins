---
name: data-table-cleanup-analyzer
description: "Table Cleanup Analyzer for Hermes Agent: apply a template workflow to table cleanup work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Table Cleanup Analyzer

Use this skill in Hermes Agent when the task involves data table cleanup analyzer. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: table cleanup data completeness, table cleanup column consistency, table cleanup outliers flagged.
2. Run the `data_table_cleanup_analyzer` tool (or follow this procedure manually) — kind: template.
3. Check the output against: table cleanup totals verified, table cleanup format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
