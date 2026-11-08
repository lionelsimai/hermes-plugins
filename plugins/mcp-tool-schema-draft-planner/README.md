# Tool Schema Draft Planner

Tool Schema Draft Planner for Hermes Agent: apply a analyze workflow to tool schema draft work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_tool_schema_draft_planner` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_tool_schema_draft_planner",
  "arguments": {
    "counts": {
      "tool_schema_draft_schema_validity": 40,
      "tool_schema_draft_description_clarity": 25,
      "tool_schema_draft_least_privilege": 10,
      "tool_schema_draft_test_coverage": 75
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
