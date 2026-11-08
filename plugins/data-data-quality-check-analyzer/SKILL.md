---
name: data-data-quality-check-analyzer
description: "Data Quality Check Analyzer for Hermes Agent: apply a checklist workflow to data quality check work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Data Quality Check Analyzer

Use this skill in Hermes Agent when the task involves data data quality check analyzer. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: data quality check data completeness, data quality check column consistency, data quality check outliers flagged.
2. Run the `data_data_quality_check_analyzer` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: data quality check totals verified, data quality check format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
