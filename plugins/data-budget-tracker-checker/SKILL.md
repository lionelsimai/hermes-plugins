---
name: data-budget-tracker-checker
description: "Budget Tracker Checker for Hermes Agent: apply a classify workflow to budget tracker work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Budget Tracker Checker

Use this skill in Hermes Agent when the task involves data budget tracker checker. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: budget tracker data completeness, budget tracker column consistency, budget tracker outliers flagged.
2. Run the `data_budget_tracker_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: budget tracker totals verified, budget tracker format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
