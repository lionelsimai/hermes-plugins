---
name: media-voiceover-script-drafter
description: "Voiceover Script Drafter for Hermes Agent: apply a score workflow to voiceover script work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Voiceover Script Drafter

Use this skill in Hermes Agent when the task involves media voiceover script drafter. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: voiceover script brief clarity, voiceover script format spec, voiceover script rights and consent.
2. Run the `media_voiceover_script_drafter` tool (or follow this procedure manually) — kind: score.
3. Check the output against: voiceover script quality gate, voiceover script approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
