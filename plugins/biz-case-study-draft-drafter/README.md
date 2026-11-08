# Case Study Draft Drafter

Case Study Draft Drafter for Hermes Agent: apply a classify workflow to case study draft work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_case_study_draft_drafter` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_case_study_draft_drafter",
  "arguments": {
    "text": "Please review: this concerns case study draft facts supplied only and case study draft approval gate."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
