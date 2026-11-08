# Meetup Agenda Drafter

Meetup Agenda Drafter for Hermes Agent: apply a audit workflow to meetup agenda work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_meetup_agenda_drafter` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_meetup_agenda_drafter",
  "arguments": {
    "text": "This sample covers meetup agenda member fit and meetup agenda tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
