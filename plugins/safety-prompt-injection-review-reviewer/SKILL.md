---
name: safety-prompt-injection-review-reviewer
description: "Prompt Injection Review Reviewer for Hermes Agent: apply a plan workflow to prompt injection review work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Prompt Injection Review Reviewer

Use this skill in Hermes Agent when the task involves safety prompt injection review reviewer. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: prompt injection review risk identified, prompt injection review approval required, prompt injection review least privilege.
2. Run the `safety_prompt_injection_review_reviewer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: prompt injection review reversibility, prompt injection review audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
