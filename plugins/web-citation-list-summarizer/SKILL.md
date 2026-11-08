---
name: web-citation-list-summarizer
description: "Citation List Summarizer for Hermes Agent: apply a prioritize workflow to citation list work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Citation List Summarizer

Use this skill in Hermes Agent when the task involves web citation list summarizer. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: citation list source quality, citation list recency, citation list corroboration.
2. Run the `web_citation_list_summarizer` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: citation list citation completeness, citation list scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
