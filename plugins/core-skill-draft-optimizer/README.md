# Skill Draft Optimizer

Skill Draft Optimizer for Hermes Agent: apply a audit workflow to skill draft work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_skill_draft_optimizer` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_skill_draft_optimizer",
  "arguments": {
    "text": "This sample covers skill draft goal clarity and skill draft setup completeness in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
