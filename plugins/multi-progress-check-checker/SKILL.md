---
name: multi-progress-check-checker
description: "Progress Check Checker for Hermes Agent: apply a prioritize workflow to progress check work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Progress Check Checker

Use this skill in Hermes Agent when the task involves multi progress check checker. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: progress check scope clarity, progress check independence of subtasks, progress check merge criteria.
2. Run the `multi_progress_check_checker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: progress check context budget, progress check verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
