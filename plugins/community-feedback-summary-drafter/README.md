# Feedback Summary Drafter

Feedback Summary Drafter for Hermes Agent: apply a analyze workflow to feedback summary work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_feedback_summary_drafter` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_feedback_summary_drafter",
  "arguments": {
    "counts": {
      "feedback_summary_member_fit": 40,
      "feedback_summary_tone_fit": 25,
      "feedback_summary_approval_gate": 10,
      "feedback_summary_safety_check": 75
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
