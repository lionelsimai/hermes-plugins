---
name: browser-multi-step-workflow-checker
description: "Multi Step Workflow Checker for Hermes Agent: apply a analyze workflow to multi step workflow work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Multi Step Workflow Checker

Use this skill in Hermes Agent when the task involves browser multi step workflow checker. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: multi step workflow step clarity, multi step workflow fallback step, multi step workflow data accuracy.
2. Run the `browser_multi_step_workflow_checker` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: multi step workflow confirmation gate, multi step workflow completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
