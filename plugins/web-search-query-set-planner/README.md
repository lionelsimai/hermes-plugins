# Search Query Set Planner

Search Query Set Planner for Hermes Agent: apply a classify workflow to search query set work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_search_query_set_planner` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_search_query_set_planner",
  "arguments": {
    "text": "Please review: this concerns search query set source quality and search query set corroboration."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
