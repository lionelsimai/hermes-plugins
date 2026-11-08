# Parallel Workstream Checker

Parallel Workstream Checker for Hermes Agent: apply a checklist workflow to parallel workstream work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_parallel_workstream_checker` (kind: checklist)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_parallel_workstream_checker",
  "arguments": {
    "completed": [
      "parallel workstream scope clarity",
      "parallel workstream independence of subtasks"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
