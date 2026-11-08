---
name: web-fact-check-extractor
description: "Fact Check Extractor for Hermes Agent: apply a classify workflow to fact check work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Fact Check Extractor

Use this skill in Hermes Agent when the task involves web fact check extractor. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: fact check source quality, fact check recency, fact check corroboration.
2. Run the `web_fact_check_extractor` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: fact check citation completeness, fact check scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
