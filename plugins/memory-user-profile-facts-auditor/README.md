# User Profile Facts Auditor

User Profile Facts Auditor for Hermes Agent: apply a prioritize workflow to user profile facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_user_profile_facts_auditor` (kind: prioritize)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_user_profile_facts_auditor",
  "arguments": {
    "items": [
      {
        "name": "Sample task A",
        "impact": 8,
        "effort": 3
      },
      {
        "name": "Sample task B",
        "impact": 6,
        "effort": 1
      }
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
