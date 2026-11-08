# Member Onboarding Checker

Member Onboarding Checker for Hermes Agent: apply a classify workflow to member onboarding work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_member_onboarding_checker` (kind: classify)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_member_onboarding_checker",
  "arguments": {
    "text": "Please review: this concerns member onboarding member fit and member onboarding approval gate."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
