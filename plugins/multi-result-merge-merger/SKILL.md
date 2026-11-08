---
name: multi-result-merge-merger
description: "Result Merge Merger for Hermes Agent: apply a audit workflow to result merge work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Result Merge Merger

Use this skill in Hermes Agent when the task involves multi result merge merger. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: result merge scope clarity, result merge independence of subtasks, result merge merge criteria.
2. Run the `multi_result_merge_merger` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: result merge context budget, result merge verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
