---
name: community-community-digest-planner
description: "Community Digest Planner for Hermes Agent: apply a score workflow to community digest work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Community Digest Planner

Use this skill in Hermes Agent when the task involves community community digest planner. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: community digest member fit, community digest tone fit, community digest approval gate.
2. Run the `community_community_digest_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: community digest safety check, community digest follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
