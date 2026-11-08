# User Profile Facts Planner

User Profile Facts Planner for Hermes Agent: apply a template workflow to user profile facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_user_profile_facts_planner` (kind: template)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_user_profile_facts_planner",
  "arguments": {
    "facts": {
      "user_profile_facts_fact_accuracy": "Sample supplied fact",
      "user_profile_facts_size_budget_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
