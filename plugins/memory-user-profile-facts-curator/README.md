# User Profile Facts Curator

User Profile Facts Curator for Hermes Agent: apply a plan workflow to user profile facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_user_profile_facts_curator` (kind: plan)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_user_profile_facts_curator",
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
