# Documentation Lookup Summarizer

Documentation Lookup Summarizer for Hermes Agent: apply a template workflow to documentation lookup work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_documentation_lookup_summarizer` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_documentation_lookup_summarizer",
  "arguments": {
    "facts": {
      "documentation_lookup_source_quality": "Sample supplied fact",
      "documentation_lookup_recency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
