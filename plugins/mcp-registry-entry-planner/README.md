# Registry Entry Planner

Registry Entry Planner for Hermes Agent: apply a analyze workflow to registry entry work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_registry_entry_planner` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_registry_entry_planner",
  "arguments": {
    "counts": {
      "registry_entry_schema_validity": 40,
      "registry_entry_description_clarity": 25,
      "registry_entry_least_privilege": 10,
      "registry_entry_test_coverage": 75
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
