---
name: biz-meeting-prep-checker
description: "Meeting Prep Checker for Hermes Agent: apply a checklist workflow to meeting prep work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Meeting Prep Checker

Use this skill in Hermes Agent when the task involves biz meeting prep checker. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: meeting prep facts supplied only, meeting prep audience fit, meeting prep approval gate.
2. Run the `biz_meeting_prep_checker` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: meeting prep next step clarity, meeting prep evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
