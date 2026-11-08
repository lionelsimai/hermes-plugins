---
name: media-video-shot-list-checker
description: "Video Shot List Checker for Hermes Agent: apply a classify workflow to video shot list work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Video Shot List Checker

Use this skill in Hermes Agent when the task involves media video shot list checker. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: video shot list brief clarity, video shot list format spec, video shot list rights and consent.
2. Run the `media_video_shot_list_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: video shot list quality gate, video shot list approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
