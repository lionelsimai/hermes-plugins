# Price Research Extractor

Price Research Extractor for Hermes Agent: apply a analyze workflow to price research work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_price_research_extractor` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_price_research_extractor",
  "arguments": {
    "counts": {
      "price_research_source_quality": 40,
      "price_research_recency": 25,
      "price_research_corroboration": 10,
      "price_research_citation_completeness": 75
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
