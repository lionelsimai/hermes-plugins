# Fact Check Planner

Fact Check Planner for Hermes Agent: apply a analyze workflow to fact check work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_fact_check_planner` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_fact_check_planner",
  "arguments": {
    "counts": {
      "fact_check_source_quality": 40,
      "fact_check_recency": 25,
      "fact_check_corroboration": 10,
      "fact_check_citation_completeness": 75
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
