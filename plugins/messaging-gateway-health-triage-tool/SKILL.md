---
name: messaging-gateway-health-triage-tool
description: "Gateway Health Triage Tool for Hermes Agent: apply a classify workflow to gateway health work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Gateway Health Triage Tool

Use this skill in Hermes Agent when the task involves messaging gateway health triage tool. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: gateway health audience fit, gateway health tone fit, gateway health length fit.
2. Run the `messaging_gateway_health_triage_tool` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: gateway health approval gate, gateway health platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
