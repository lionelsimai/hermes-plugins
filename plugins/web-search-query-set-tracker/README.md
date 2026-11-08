# Search Query Set Tracker

Search Query Set Tracker for Hermes Agent: apply a score workflow to search query set work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_search_query_set_tracker` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_search_query_set_tracker",
  "arguments": {
    "metrics": {
      "search_query_set_source_quality": 80,
      "search_query_set_recency": 65,
      "search_query_set_corroboration": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
