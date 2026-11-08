---
name: multi-research-delegation-merger
description: "Research Delegation Merger for Hermes Agent: apply a prioritize workflow to research delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Research Delegation Merger

Use this skill in Hermes Agent when the task involves multi research delegation merger. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: research delegation scope clarity, research delegation independence of subtasks, research delegation merge criteria.
2. Run the `multi_research_delegation_merger` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: research delegation context budget, research delegation verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
