# Model Routing Auditor

Model Routing Auditor for Hermes Agent: apply a score workflow to model routing work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_model_routing_auditor` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_model_routing_auditor",
  "arguments": {
    "metrics": {
      "model_routing_goal_clarity": 80,
      "model_routing_setup_completeness": 65,
      "model_routing_toolset_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
