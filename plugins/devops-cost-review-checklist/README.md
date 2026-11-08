# Cost Review Checklist

Cost Review Checklist for Hermes Agent: apply a prioritize workflow to cost review work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_cost_review_checklist` (kind: prioritize)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_cost_review_checklist",
  "arguments": {
    "items": [
      {
        "name": "Sample task A",
        "impact": 8,
        "effort": 3
      },
      {
        "name": "Sample task B",
        "impact": 6,
        "effort": 1
      }
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
