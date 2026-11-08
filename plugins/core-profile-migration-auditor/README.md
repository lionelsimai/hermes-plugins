# Profile Migration Auditor

Profile Migration Auditor for Hermes Agent: apply a checklist workflow to profile migration work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_profile_migration_auditor` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_profile_migration_auditor",
  "arguments": {
    "completed": [
      "profile migration goal clarity",
      "profile migration setup completeness"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
