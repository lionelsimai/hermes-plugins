# Feedback Summary Checker

Feedback Summary Checker for Hermes Agent: apply a audit workflow to feedback summary work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_feedback_summary_checker` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_feedback_summary_checker",
  "arguments": {
    "text": "This sample covers feedback summary member fit and feedback summary tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
