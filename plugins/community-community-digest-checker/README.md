# Community Digest Checker

Community Digest Checker for Hermes Agent: apply a analyze workflow to community digest work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_community_digest_checker` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_community_digest_checker",
  "arguments": {
    "counts": {
      "community_digest_member_fit": 40,
      "community_digest_tone_fit": 25,
      "community_digest_approval_gate": 10,
      "community_digest_safety_check": 75
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
