# Agent Profile Builder

Agent Profile Builder for Hermes Agent: apply a score workflow to agent profile work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_agent_profile_builder` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_agent_profile_builder",
  "arguments": {
    "metrics": {
      "agent_profile_goal_clarity": 80,
      "agent_profile_setup_completeness": 65,
      "agent_profile_toolset_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
