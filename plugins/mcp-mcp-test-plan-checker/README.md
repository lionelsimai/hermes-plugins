# Mcp Test Plan Checker

Mcp Test Plan Checker for Hermes Agent: apply a analyze workflow to mcp test plan work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_test_plan_checker` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_test_plan_checker",
  "arguments": {
    "counts": {
      "mcp_test_plan_schema_validity": 40,
      "mcp_test_plan_description_clarity": 25,
      "mcp_test_plan_least_privilege": 10,
      "mcp_test_plan_test_coverage": 75
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
