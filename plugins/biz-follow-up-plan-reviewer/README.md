# Follow Up Plan Reviewer

Follow Up Plan Reviewer for Hermes Agent: apply a checklist workflow to follow up plan work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_follow_up_plan_reviewer` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_follow_up_plan_reviewer",
  "arguments": {
    "completed": [
      "follow up plan facts supplied only",
      "follow up plan audience fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
