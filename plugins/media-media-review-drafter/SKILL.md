---
name: media-media-review-drafter
description: "Media Review Drafter for Hermes Agent: apply a analyze workflow to media review work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Media Review Drafter

Use this skill in Hermes Agent when the task involves media media review drafter. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: media review brief clarity, media review format spec, media review rights and consent.
2. Run the `media_media_review_drafter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: media review quality gate, media review approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
