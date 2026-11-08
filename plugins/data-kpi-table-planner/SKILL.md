---
name: data-kpi-table-planner
description: "Kpi Table Planner for Hermes Agent: apply a analyze workflow to kpi table work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Kpi Table Planner

Use this skill in Hermes Agent when the task involves data kpi table planner. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: kpi table data completeness, kpi table column consistency, kpi table outliers flagged.
2. Run the `data_kpi_table_planner` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: kpi table totals verified, kpi table format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
