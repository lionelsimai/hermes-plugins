# Incident Notes Checklist

Incident Notes Checklist for Hermes Agent: apply a checklist workflow to incident notes work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_incident_notes_checklist` (kind: checklist)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_incident_notes_checklist",
  "arguments": {
    "completed": [
      "incident notes risk noted",
      "incident notes rollback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
