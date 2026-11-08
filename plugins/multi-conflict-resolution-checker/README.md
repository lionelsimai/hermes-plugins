# Conflict Resolution Checker

Conflict Resolution Checker for Hermes Agent: apply a template workflow to conflict resolution work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_conflict_resolution_checker` (kind: template)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_conflict_resolution_checker",
  "arguments": {
    "facts": {
      "conflict_resolution_scope_clarity": "Sample supplied fact",
      "conflict_resolution_independence_of_subtasks": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
