---
name: browser-login-flow-check-sequencer
description: "Login Flow Check Sequencer for Hermes Agent: apply a classify workflow to login flow check work — covers step clarity, fallback step and completion proof, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Hermes, Plugins]
    category: browser-automation
---

# Login Flow Check Sequencer

Use this skill in Hermes Agent when the task involves browser login flow check sequencer. It sits in the Browser Automation category; the suggested Hermes toolset is `browser`.

## Workflow
1. Confirm the goal and gather supplied facts about: login flow check step clarity, login flow check fallback step, login flow check data accuracy.
2. Run the `browser_login_flow_check_sequencer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: login flow check confirmation gate, login flow check completion proof.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
