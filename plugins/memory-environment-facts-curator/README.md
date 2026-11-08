# Environment Facts Curator

Environment Facts Curator for Hermes Agent: apply a audit workflow to environment facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_environment_facts_curator` (kind: audit)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_environment_facts_curator",
  "arguments": {
    "text": "This sample covers environment facts fact accuracy and environment facts size budget fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
