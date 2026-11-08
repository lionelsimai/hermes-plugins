---
name: browser-upload-task-auditor
description: "Upload Task Auditor for Hermes Agent: apply a prioritize workflow to upload task work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Upload Task Auditor

Use this skill in Hermes Agent when the task involves browser upload task auditor. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: upload task step clarity, upload task fallback step, upload task data accuracy.
2. Run the `browser_upload_task_auditor` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: upload task confirmation gate, upload task completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
