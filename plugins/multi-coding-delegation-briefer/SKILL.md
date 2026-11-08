---
name: multi-coding-delegation-briefer
description: "Coding Delegation Briefer for Hermes Agent: apply a analyze workflow to coding delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Coding Delegation Briefer

Use this skill in Hermes Agent when the task involves multi coding delegation briefer. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: coding delegation scope clarity, coding delegation independence of subtasks, coding delegation merge criteria.
2. Run the `multi_coding_delegation_briefer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: coding delegation context budget, coding delegation verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
