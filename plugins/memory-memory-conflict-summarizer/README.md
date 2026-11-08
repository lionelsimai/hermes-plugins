# Memory Conflict Summarizer

Memory Conflict Summarizer for Hermes Agent: apply a plan workflow to memory conflict work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_memory_conflict_summarizer` (kind: plan)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_memory_conflict_summarizer",
  "arguments": {
    "goal": "Sample goal for this workflow",
    "timeframe_days": 14
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
