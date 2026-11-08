# Memory Conflict Auditor

Memory Conflict Auditor for Hermes Agent: apply a audit workflow to memory conflict work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_memory_conflict_auditor` (kind: audit)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_memory_conflict_auditor",
  "arguments": {
    "text": "This sample covers memory conflict fact accuracy and memory conflict size budget fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
