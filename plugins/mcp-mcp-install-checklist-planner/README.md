# Mcp Install Checklist Planner

Mcp Install Checklist Planner for Hermes Agent: apply a score workflow to mcp install checklist work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_install_checklist_planner` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_install_checklist_planner",
  "arguments": {
    "metrics": {
      "mcp_install_checklist_schema_validity": 80,
      "mcp_install_checklist_description_clarity": 65,
      "mcp_install_checklist_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
