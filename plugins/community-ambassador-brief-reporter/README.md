# Ambassador Brief Reporter

Ambassador Brief Reporter for Hermes Agent: apply a analyze workflow to ambassador brief work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_ambassador_brief_reporter` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_ambassador_brief_reporter",
  "arguments": {
    "counts": {
      "ambassador_brief_member_fit": 40,
      "ambassador_brief_tone_fit": 25,
      "ambassador_brief_approval_gate": 10,
      "ambassador_brief_safety_check": 75
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
