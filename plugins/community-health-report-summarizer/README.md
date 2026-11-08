# Health Report Summarizer

Health Report Summarizer for Hermes Agent: apply a score workflow to health report work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_health_report_summarizer` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_health_report_summarizer",
  "arguments": {
    "metrics": {
      "health_report_member_fit": 80,
      "health_report_tone_fit": 65,
      "health_report_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
