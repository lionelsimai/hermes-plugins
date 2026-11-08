---
name: prod-decision-log-tracker
description: "Decision Log Tracker for Hermes Agent: apply a score workflow to decision log work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Decision Log Tracker

Use this skill in Hermes Agent when the task involves prod decision log tracker. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: decision log priority clarity, decision log time realism, decision log next action named.
2. Run the `prod_decision_log_tracker` tool (or follow this procedure manually) — kind: score.
3. Check the output against: decision log review cadence, decision log owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
