---
name: media-diagram-brief-planner
description: "Diagram Brief Planner for Hermes Agent: apply a template workflow to diagram brief work — covers brief clarity, format spec and approval gate, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Media (Image Audio Video), Hermes, Plugins]
    category: media-image-audio-video
---

# Diagram Brief Planner

Use this skill in Hermes Agent when the task involves media diagram brief planner. It sits in the Media (Image Audio Video) category; the suggested Hermes toolset is `media`.

## Workflow
1. Confirm the goal and gather supplied facts about: diagram brief brief clarity, diagram brief format spec, diagram brief rights and consent.
2. Run the `media_diagram_brief_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: diagram brief quality gate, diagram brief approval gate.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
