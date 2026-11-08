# Speaker Brief Planner

Speaker Brief Planner for Hermes Agent: apply a analyze workflow to speaker brief work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_speaker_brief_planner` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_speaker_brief_planner",
  "arguments": {
    "counts": {
      "speaker_brief_member_fit": 40,
      "speaker_brief_tone_fit": 25,
      "speaker_brief_approval_gate": 10,
      "speaker_brief_safety_check": 75
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
