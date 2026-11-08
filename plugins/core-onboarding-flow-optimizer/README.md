# Onboarding Flow Optimizer

Onboarding Flow Optimizer for Hermes Agent: apply a checklist workflow to onboarding flow work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_onboarding_flow_optimizer` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_onboarding_flow_optimizer",
  "arguments": {
    "completed": [
      "onboarding flow goal clarity",
      "onboarding flow setup completeness"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
