# Documentation Lookup Extractor

Documentation Lookup Extractor for Hermes Agent: apply a score workflow to documentation lookup work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_documentation_lookup_extractor` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_documentation_lookup_extractor",
  "arguments": {
    "metrics": {
      "documentation_lookup_source_quality": 80,
      "documentation_lookup_recency": 65,
      "documentation_lookup_corroboration": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
