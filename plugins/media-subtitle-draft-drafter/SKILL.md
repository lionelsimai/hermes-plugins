---
name: media-subtitle-draft-drafter
description: "Subtitle Draft Drafter for Hermes Agent: apply a prioritize workflow to subtitle draft work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Subtitle Draft Drafter

Use this skill in Hermes Agent when the task involves media subtitle draft drafter. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: subtitle draft brief clarity, subtitle draft format spec, subtitle draft rights and consent.
2. Run the `media_subtitle_draft_drafter` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: subtitle draft quality gate, subtitle draft approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
