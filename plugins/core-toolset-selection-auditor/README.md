# Toolset Selection Auditor

Toolset Selection Auditor for Hermes Agent: apply a analyze workflow to toolset selection work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_toolset_selection_auditor` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_toolset_selection_auditor",
  "arguments": {
    "counts": {
      "toolset_selection_goal_clarity": 40,
      "toolset_selection_setup_completeness": 25,
      "toolset_selection_toolset_fit": 10,
      "toolset_selection_guardrail_coverage": 75
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
