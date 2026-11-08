# Meeting Prep Drafter

Meeting Prep Drafter for Hermes Agent: apply a template workflow to meeting prep work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_meeting_prep_drafter` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_meeting_prep_drafter",
  "arguments": {
    "facts": {
      "meeting_prep_facts_supplied_only": "Sample supplied fact",
      "meeting_prep_audience_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
