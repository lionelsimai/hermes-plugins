# User Profile Facts Summarizer

User Profile Facts Summarizer for Hermes Agent: apply a score workflow to user profile facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_user_profile_facts_summarizer` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_user_profile_facts_summarizer",
  "arguments": {
    "metrics": {
      "user_profile_facts_fact_accuracy": 80,
      "user_profile_facts_size_budget_fit": 65,
      "user_profile_facts_staleness": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
