# Session Setup Builder

Session Setup Builder for Hermes Agent: apply a audit workflow to session setup work — covers goal clarity, setup completeness and verification step, using supplied facts only.

- Category: Core Agent Ops & Skill Authoring
- Tool: `core_session_setup_builder` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "core_session_setup_builder",
  "arguments": {
    "text": "This sample covers session setup goal clarity and session setup setup completeness in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
