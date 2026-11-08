# Toolset Selection Builder

Toolset Selection Builder for Hermes Agent: apply a template workflow to toolset selection work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_toolset_selection_builder` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_toolset_selection_builder",
  "arguments": {
    "facts": {
      "toolset_selection_goal_clarity": "Sample supplied fact",
      "toolset_selection_setup_completeness": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
