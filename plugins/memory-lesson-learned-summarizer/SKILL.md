---
name: memory-lesson-learned-summarizer
description: "Lesson Learned Summarizer for Hermes Agent: apply a classify workflow to lesson learned work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Lesson Learned Summarizer

Use this skill in Hermes Agent when the task involves memory lesson learned summarizer. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: lesson learned fact accuracy, lesson learned size budget fit, lesson learned staleness.
2. Run the `memory_lesson_learned_summarizer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: lesson learned duplication, lesson learned source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
