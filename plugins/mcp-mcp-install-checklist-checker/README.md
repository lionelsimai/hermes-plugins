# Mcp Install Checklist Checker

Mcp Install Checklist Checker for Hermes Agent: apply a checklist workflow to mcp install checklist work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_install_checklist_checker` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_install_checklist_checker",
  "arguments": {
    "completed": [
      "mcp install checklist schema validity",
      "mcp install checklist description clarity"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
