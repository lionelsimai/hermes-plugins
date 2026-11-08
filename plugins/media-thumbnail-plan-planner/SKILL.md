---
name: media-thumbnail-plan-planner
description: "Thumbnail Plan Planner for Hermes Agent: apply a classify workflow to thumbnail plan work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Thumbnail Plan Planner

Use this skill in Hermes Agent when the task involves media thumbnail plan planner. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: thumbnail plan brief clarity, thumbnail plan format spec, thumbnail plan rights and consent.
2. Run the `media_thumbnail_plan_planner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: thumbnail plan quality gate, thumbnail plan approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
