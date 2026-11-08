---
name: data-survey-results-analyzer
description: "Survey Results Analyzer for Hermes Agent: apply a plan workflow to survey results work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Survey Results Analyzer

Use this skill in Hermes Agent when the task involves data survey results analyzer. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: survey results data completeness, survey results column consistency, survey results outliers flagged.
2. Run the `data_survey_results_analyzer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: survey results totals verified, survey results format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
