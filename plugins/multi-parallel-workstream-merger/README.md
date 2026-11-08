# Parallel Workstream Merger

Parallel Workstream Merger for Hermes Agent: apply a score workflow to parallel workstream work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_parallel_workstream_merger` (kind: score)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_parallel_workstream_merger",
  "arguments": {
    "metrics": {
      "parallel_workstream_scope_clarity": 80,
      "parallel_workstream_independence_of_subtasks": 65,
      "parallel_workstream_merge_criteria": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
