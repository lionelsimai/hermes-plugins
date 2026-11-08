---
name: media-video-shot-list-drafter
description: "Video Shot List Drafter for Hermes Agent: apply a template workflow to video shot list work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Video Shot List Drafter

Use this skill in Hermes Agent when the task involves media video shot list drafter. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: video shot list brief clarity, video shot list format spec, video shot list rights and consent.
2. Run the `media_video_shot_list_drafter` tool (or follow this procedure manually) — kind: template.
3. Check the output against: video shot list quality gate, video shot list approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
