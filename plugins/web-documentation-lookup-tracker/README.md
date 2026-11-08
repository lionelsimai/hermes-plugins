# Documentation Lookup Tracker

Documentation Lookup Tracker for Hermes Agent: apply a analyze workflow to documentation lookup work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_documentation_lookup_tracker` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_documentation_lookup_tracker",
  "arguments": {
    "counts": {
      "documentation_lookup_source_quality": 40,
      "documentation_lookup_recency": 25,
      "documentation_lookup_corroboration": 10,
      "documentation_lookup_citation_completeness": 75
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
