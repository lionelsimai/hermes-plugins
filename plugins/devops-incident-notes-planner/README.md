# Incident Notes Planner

Incident Notes Planner for Hermes Agent: apply a classify workflow to incident notes work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_incident_notes_planner` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_incident_notes_planner",
  "arguments": {
    "text": "Please review: this concerns incident notes risk noted and incident notes verification."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
