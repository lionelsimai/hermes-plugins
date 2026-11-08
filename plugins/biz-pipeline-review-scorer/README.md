# Pipeline Review Scorer

Pipeline Review Scorer for Hermes Agent: apply a score workflow to pipeline review work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_pipeline_review_scorer` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_pipeline_review_scorer",
  "arguments": {
    "metrics": {
      "pipeline_review_facts_supplied_only": 80,
      "pipeline_review_audience_fit": 65,
      "pipeline_review_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
