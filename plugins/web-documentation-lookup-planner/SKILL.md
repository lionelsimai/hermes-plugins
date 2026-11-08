---
name: web-documentation-lookup-planner
description: "Documentation Lookup Planner for Hermes Agent: apply a prioritize workflow to documentation lookup work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Documentation Lookup Planner

Use this skill in Hermes Agent when the task involves web documentation lookup planner. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: documentation lookup source quality, documentation lookup recency, documentation lookup corroboration.
2. Run the `web_documentation_lookup_planner` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: documentation lookup citation completeness, documentation lookup scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
