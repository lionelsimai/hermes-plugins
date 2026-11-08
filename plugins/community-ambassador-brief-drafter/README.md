# Ambassador Brief Drafter

Ambassador Brief Drafter for Hermes Agent: apply a score workflow to ambassador brief work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_ambassador_brief_drafter` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_ambassador_brief_drafter",
  "arguments": {
    "metrics": {
      "ambassador_brief_member_fit": 80,
      "ambassador_brief_tone_fit": 65,
      "ambassador_brief_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
