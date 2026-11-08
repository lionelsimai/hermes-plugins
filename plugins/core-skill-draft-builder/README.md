# Skill Draft Builder

Skill Draft Builder for Hermes Agent: apply a checklist workflow to skill draft work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_skill_draft_builder` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_skill_draft_builder",
  "arguments": {
    "completed": [
      "skill draft goal clarity",
      "skill draft setup completeness"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
