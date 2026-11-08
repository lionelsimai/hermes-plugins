---
name: prod-reading-list-reviewer
description: "Reading List Reviewer for Hermes Agent: apply a template workflow to reading list work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Reading List Reviewer

Use this skill in Hermes Agent when the task involves prod reading list reviewer. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: reading list priority clarity, reading list time realism, reading list next action named.
2. Run the `prod_reading_list_reviewer` tool (or follow this procedure manually) — kind: template.
3. Check the output against: reading list review cadence, reading list owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
