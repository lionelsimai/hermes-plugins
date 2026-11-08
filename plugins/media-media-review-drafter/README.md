# Media Review Drafter

Media Review Drafter for Hermes Agent: apply a analyze workflow to media review work — covers brief clarity, format spec and approval gate, using supplied facts only.

- Category: Media (Image Audio Video)
- Tool: `media_media_review_drafter` (kind: analyze)
- Suggested Hermes toolset: `media`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "media_media_review_drafter",
  "arguments": {
    "counts": {
      "media_review_brief_clarity": 40,
      "media_review_format_spec": 25,
      "media_review_rights_and_consent": 10,
      "media_review_quality_gate": 75
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
