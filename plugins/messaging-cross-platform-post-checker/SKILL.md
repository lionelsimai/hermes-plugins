---
name: messaging-cross-platform-post-checker
description: "Cross Platform Post Checker for Hermes Agent: apply a template workflow to cross platform post work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Cross Platform Post Checker

Use this skill in Hermes Agent when the task involves messaging cross platform post checker. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: cross platform post audience fit, cross platform post tone fit, cross platform post length fit.
2. Run the `messaging_cross_platform_post_checker` tool (or follow this procedure manually) — kind: template.
3. Check the output against: cross platform post approval gate, cross platform post platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
