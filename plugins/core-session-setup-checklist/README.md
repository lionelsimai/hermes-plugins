# Session Setup Checklist

Session Setup Checklist for Hermes Agent: apply a score workflow to session setup work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_session_setup_checklist` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_session_setup_checklist",
  "arguments": {
    "metrics": {
      "session_setup_goal_clarity": 80,
      "session_setup_setup_completeness": 65,
      "session_setup_toolset_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
