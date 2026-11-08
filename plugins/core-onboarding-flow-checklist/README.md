# Onboarding Flow Checklist

Onboarding Flow Checklist for Hermes Agent: apply a score workflow to onboarding flow work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_onboarding_flow_checklist` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_onboarding_flow_checklist",
  "arguments": {
    "metrics": {
      "onboarding_flow_goal_clarity": 80,
      "onboarding_flow_setup_completeness": 65,
      "onboarding_flow_toolset_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
