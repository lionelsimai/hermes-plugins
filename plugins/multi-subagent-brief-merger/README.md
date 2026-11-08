# Subagent Brief Merger

Subagent Brief Merger for Hermes Agent: apply a analyze workflow to subagent brief work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_subagent_brief_merger` (kind: analyze)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_subagent_brief_merger",
  "arguments": {
    "counts": {
      "subagent_brief_scope_clarity": 40,
      "subagent_brief_independence_of_subtasks": 25,
      "subagent_brief_merge_criteria": 10,
      "subagent_brief_context_budget": 75
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
