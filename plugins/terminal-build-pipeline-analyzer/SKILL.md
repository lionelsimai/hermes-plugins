---
name: terminal-build-pipeline-analyzer
description: "Build Pipeline Analyzer for Hermes Agent: apply a analyze workflow to build pipeline work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Build Pipeline Analyzer

Use this skill in Hermes Agent when the task involves terminal build pipeline analyzer. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: build pipeline command safety, build pipeline expected output, build pipeline timeout set.
2. Run the `terminal_build_pipeline_analyzer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: build pipeline rollback step, build pipeline verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
