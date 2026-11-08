---
name: prod-habit-tracker-planner
description: "Habit Tracker Planner for Hermes Agent: apply a analyze workflow to habit tracker work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Habit Tracker Planner

Use this skill in Hermes Agent when the task involves prod habit tracker planner. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: habit tracker priority clarity, habit tracker time realism, habit tracker next action named.
2. Run the `prod_habit_tracker_planner` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: habit tracker review cadence, habit tracker owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
