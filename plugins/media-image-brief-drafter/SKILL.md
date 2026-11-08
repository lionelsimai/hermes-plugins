---
name: media-image-brief-drafter
description: "Image Brief Drafter for Hermes Agent: apply a plan workflow to image brief work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Image Brief Drafter

Use this skill in Hermes Agent when the task involves media image brief drafter. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: image brief brief clarity, image brief format spec, image brief rights and consent.
2. Run the `media_image_brief_drafter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: image brief quality gate, image brief approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
