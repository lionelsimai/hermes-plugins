# Research Delegation Checker

Research Delegation Checker for Hermes Agent: apply a score workflow to research delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_research_delegation_checker` (kind: score)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_research_delegation_checker",
  "arguments": {
    "metrics": {
      "research_delegation_scope_clarity": 80,
      "research_delegation_independence_of_subtasks": 65,
      "research_delegation_merge_criteria": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
