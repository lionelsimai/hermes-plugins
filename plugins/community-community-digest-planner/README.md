# Community Digest Planner

Community Digest Planner for Hermes Agent: apply a score workflow to community digest work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_community_digest_planner` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_community_digest_planner",
  "arguments": {
    "metrics": {
      "community_digest_member_fit": 80,
      "community_digest_tone_fit": 65,
      "community_digest_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
