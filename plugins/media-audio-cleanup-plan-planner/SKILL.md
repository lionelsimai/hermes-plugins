---
name: media-audio-cleanup-plan-planner
description: "Audio Cleanup Plan Planner for Hermes Agent: apply a audit workflow to audio cleanup plan work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Audio Cleanup Plan Planner

Use this skill in Hermes Agent when the task involves media audio cleanup plan planner. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: audio cleanup plan brief clarity, audio cleanup plan format spec, audio cleanup plan rights and consent.
2. Run the `media_audio_cleanup_plan_planner` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: audio cleanup plan quality gate, audio cleanup plan approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
