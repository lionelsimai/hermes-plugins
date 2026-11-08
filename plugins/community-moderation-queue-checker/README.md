# Moderation Queue Checker

Moderation Queue Checker for Hermes Agent: apply a score workflow to moderation queue work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_moderation_queue_checker` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_moderation_queue_checker",
  "arguments": {
    "metrics": {
      "moderation_queue_member_fit": 80,
      "moderation_queue_tone_fit": 65,
      "moderation_queue_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
