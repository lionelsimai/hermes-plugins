---
name: browser-form-fill-plan-checker
description: "Form Fill Plan Checker for Hermes Agent: apply a plan workflow to form fill plan work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Form Fill Plan Checker

Use this skill in Hermes Agent when the task involves browser form fill plan checker. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: form fill plan step clarity, form fill plan fallback step, form fill plan data accuracy.
2. Run the `browser_form_fill_plan_checker` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: form fill plan confirmation gate, form fill plan completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
