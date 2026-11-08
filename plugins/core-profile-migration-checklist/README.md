# Profile Migration Checklist

Profile Migration Checklist for Hermes Agent: apply a analyze workflow to profile migration work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_profile_migration_checklist` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_profile_migration_checklist",
  "arguments": {
    "counts": {
      "profile_migration_goal_clarity": 40,
      "profile_migration_setup_completeness": 25,
      "profile_migration_toolset_fit": 10,
      "profile_migration_guardrail_coverage": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
