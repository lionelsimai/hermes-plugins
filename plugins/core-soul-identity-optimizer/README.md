# Soul Identity Optimizer

Soul Identity Optimizer for Hermes Agent: apply a score workflow to SOUL identity work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_soul_identity_optimizer` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_soul_identity_optimizer",
  "arguments": {
    "metrics": {
      "soul_identity_goal_clarity": 80,
      "soul_identity_setup_completeness": 65,
      "soul_identity_toolset_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
