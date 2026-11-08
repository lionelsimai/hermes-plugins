# Project Facts Auditor

Project Facts Auditor for Hermes Agent: apply a classify workflow to project facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_project_facts_auditor` (kind: classify)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_project_facts_auditor",
  "arguments": {
    "text": "Please review: this concerns project facts fact accuracy and project facts staleness."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
