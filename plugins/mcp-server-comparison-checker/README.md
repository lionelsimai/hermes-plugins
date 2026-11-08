# Server Comparison Checker

Server Comparison Checker for Hermes Agent: apply a score workflow to server comparison work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_server_comparison_checker` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_server_comparison_checker",
  "arguments": {
    "metrics": {
      "server_comparison_schema_validity": 80,
      "server_comparison_description_clarity": 65,
      "server_comparison_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
