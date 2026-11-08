# Source Shortlist Verifier

Source Shortlist Verifier for Hermes Agent: apply a analyze workflow to source shortlist work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_source_shortlist_verifier` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_source_shortlist_verifier",
  "arguments": {
    "counts": {
      "source_shortlist_source_quality": 40,
      "source_shortlist_recency": 25,
      "source_shortlist_corroboration": 10,
      "source_shortlist_citation_completeness": 75
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
