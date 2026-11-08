# Mcp Server Review Reviewer

Mcp Server Review Reviewer for Hermes Agent: apply a analyze workflow to mcp server review work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_server_review_reviewer` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_server_review_reviewer",
  "arguments": {
    "counts": {
      "mcp_server_review_schema_validity": 40,
      "mcp_server_review_description_clarity": 25,
      "mcp_server_review_least_privilege": 10,
      "mcp_server_review_test_coverage": 75
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
