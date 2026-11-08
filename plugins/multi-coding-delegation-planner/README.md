# Coding Delegation Planner

Coding Delegation Planner for Hermes Agent: apply a template workflow to coding delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_coding_delegation_planner` (kind: template)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_coding_delegation_planner",
  "arguments": {
    "facts": {
      "coding_delegation_scope_clarity": "Sample supplied fact",
      "coding_delegation_independence_of_subtasks": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
