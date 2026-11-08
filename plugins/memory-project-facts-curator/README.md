# Project Facts Curator

Project Facts Curator for Hermes Agent: apply a analyze workflow to project facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_project_facts_curator` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_project_facts_curator",
  "arguments": {
    "counts": {
      "project_facts_fact_accuracy": 40,
      "project_facts_size_budget_fit": 25,
      "project_facts_staleness": 10,
      "project_facts_duplication": 75
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
