# Meetup Agenda Reporter

Meetup Agenda Reporter for Hermes Agent: apply a score workflow to meetup agenda work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_meetup_agenda_reporter` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_meetup_agenda_reporter",
  "arguments": {
    "metrics": {
      "meetup_agenda_member_fit": 80,
      "meetup_agenda_tone_fit": 65,
      "meetup_agenda_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
