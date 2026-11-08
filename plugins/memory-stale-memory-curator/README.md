# Stale Memory Curator

Stale Memory Curator for Hermes Agent: apply a checklist workflow to stale memory work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_stale_memory_curator` (kind: checklist)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_stale_memory_curator",
  "arguments": {
    "completed": [
      "stale memory fact accuracy",
      "stale memory size budget fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
