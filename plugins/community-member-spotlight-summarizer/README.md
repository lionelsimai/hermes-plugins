# Member Spotlight Summarizer

Member Spotlight Summarizer for Hermes Agent: apply a analyze workflow to member spotlight work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_member_spotlight_summarizer` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_member_spotlight_summarizer",
  "arguments": {
    "counts": {
      "member_spotlight_member_fit": 40,
      "member_spotlight_tone_fit": 25,
      "member_spotlight_approval_gate": 10,
      "member_spotlight_safety_check": 75
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
