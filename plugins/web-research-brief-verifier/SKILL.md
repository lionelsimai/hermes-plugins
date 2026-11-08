---
name: web-research-brief-verifier
description: "Research Brief Verifier for Hermes Agent: apply a analyze workflow to research brief work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Research Brief Verifier

Use this skill in Hermes Agent when the task involves web research brief verifier. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: research brief source quality, research brief recency, research brief corroboration.
2. Run the `web_research_brief_verifier` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: research brief citation completeness, research brief scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
