---
name: data-chart-brief-planner
description: "Chart Brief Planner for Hermes Agent: apply a prioritize workflow to chart brief work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Chart Brief Planner

Use this skill in Hermes Agent when the task involves data chart brief planner. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: chart brief data completeness, chart brief column consistency, chart brief outliers flagged.
2. Run the `data_chart_brief_planner` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: chart brief totals verified, chart brief format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
