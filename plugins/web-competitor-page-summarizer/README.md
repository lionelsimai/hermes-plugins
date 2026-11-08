# Competitor Page Summarizer

Competitor Page Summarizer for Hermes Agent: apply a analyze workflow to competitor page work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_competitor_page_summarizer` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_competitor_page_summarizer",
  "arguments": {
    "counts": {
      "competitor_page_source_quality": 40,
      "competitor_page_recency": 25,
      "competitor_page_corroboration": 10,
      "competitor_page_citation_completeness": 75
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
