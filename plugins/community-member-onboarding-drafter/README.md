# Member Onboarding Drafter

Member Onboarding Drafter for Hermes Agent: apply a template workflow to member onboarding work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_member_onboarding_drafter` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_member_onboarding_drafter",
  "arguments": {
    "facts": {
      "member_onboarding_member_fit": "Sample supplied fact",
      "member_onboarding_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
