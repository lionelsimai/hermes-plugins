---
name: web-fact-check-tracker
description: "Fact Check Tracker for Hermes Agent: apply a prioritize workflow to fact check work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Fact Check Tracker

Use this skill in Hermes Agent when the task involves web fact check tracker. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: fact check source quality, fact check recency, fact check corroboration.
2. Run the `web_fact_check_tracker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: fact check citation completeness, fact check scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
