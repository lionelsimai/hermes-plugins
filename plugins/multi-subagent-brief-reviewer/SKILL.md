---
name: multi-subagent-brief-reviewer
description: "Subagent Brief Reviewer for Hermes Agent: apply a audit workflow to subagent brief work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Subagent Brief Reviewer

Use this skill in Hermes Agent when the task involves multi subagent brief reviewer. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: subagent brief scope clarity, subagent brief independence of subtasks, subagent brief merge criteria.
2. Run the `multi_subagent_brief_reviewer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: subagent brief context budget, subagent brief verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
