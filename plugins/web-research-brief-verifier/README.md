# Research Brief Verifier

Research Brief Verifier for Hermes Agent: apply a analyze workflow to research brief work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_research_brief_verifier` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_research_brief_verifier",
  "arguments": {
    "counts": {
      "research_brief_source_quality": 40,
      "research_brief_recency": 25,
      "research_brief_corroboration": 10,
      "research_brief_citation_completeness": 75
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
