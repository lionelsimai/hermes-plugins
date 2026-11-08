# Meeting Prep Reviewer

Meeting Prep Reviewer for Hermes Agent: apply a classify workflow to meeting prep work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_meeting_prep_reviewer` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_meeting_prep_reviewer",
  "arguments": {
    "text": "Please review: this concerns meeting prep facts supplied only and meeting prep approval gate."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
