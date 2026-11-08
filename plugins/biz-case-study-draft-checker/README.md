# Case Study Draft Checker

Case Study Draft Checker for Hermes Agent: apply a analyze workflow to case study draft work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_case_study_draft_checker` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_case_study_draft_checker",
  "arguments": {
    "counts": {
      "case_study_draft_facts_supplied_only": 40,
      "case_study_draft_audience_fit": 25,
      "case_study_draft_approval_gate": 10,
      "case_study_draft_next_step_clarity": 75
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
