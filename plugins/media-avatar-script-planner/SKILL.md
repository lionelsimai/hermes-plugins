---
name: media-avatar-script-planner
description: "Avatar Script Planner for Hermes Agent: apply a prioritize workflow to avatar script work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Avatar Script Planner

Use this skill in Hermes Agent when the task involves media avatar script planner. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: avatar script brief clarity, avatar script format spec, avatar script rights and consent.
2. Run the `media_avatar_script_planner` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: avatar script quality gate, avatar script approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
