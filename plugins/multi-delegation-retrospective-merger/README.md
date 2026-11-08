# Delegation Retrospective Merger

Delegation Retrospective Merger for Hermes Agent: apply a analyze workflow to delegation retrospective work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_delegation_retrospective_merger` (kind: analyze)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_delegation_retrospective_merger",
  "arguments": {
    "counts": {
      "delegation_retrospective_scope_clarity": 40,
      "delegation_retrospective_independence_of_subtasks": 25,
      "delegation_retrospective_merge_criteria": 10,
      "delegation_retrospective_context_budget": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
