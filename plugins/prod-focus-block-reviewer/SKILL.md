---
name: prod-focus-block-reviewer
description: "Focus Block Reviewer for Hermes Agent: apply a analyze workflow to focus block work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Focus Block Reviewer

Use this skill in Hermes Agent when the task involves prod focus block reviewer. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: focus block priority clarity, focus block time realism, focus block next action named.
2. Run the `prod_focus_block_reviewer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: focus block review cadence, focus block owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
