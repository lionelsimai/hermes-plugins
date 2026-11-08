# Session Memory Summarizer

Session Memory Summarizer for Hermes Agent: apply a analyze workflow to session memory work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_session_memory_summarizer` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_session_memory_summarizer",
  "arguments": {
    "counts": {
      "session_memory_fact_accuracy": 40,
      "session_memory_size_budget_fit": 25,
      "session_memory_staleness": 10,
      "session_memory_duplication": 75
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
