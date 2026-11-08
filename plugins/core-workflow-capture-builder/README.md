# Workflow Capture Builder

Workflow Capture Builder for Hermes Agent: apply a analyze workflow to workflow capture work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_workflow_capture_builder` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_workflow_capture_builder",
  "arguments": {
    "counts": {
      "workflow_capture_goal_clarity": 40,
      "workflow_capture_setup_completeness": 25,
      "workflow_capture_toolset_fit": 10,
      "workflow_capture_guardrail_coverage": 75
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
