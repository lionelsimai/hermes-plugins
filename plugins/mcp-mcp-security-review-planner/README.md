# Mcp Security Review Planner

Mcp Security Review Planner for Hermes Agent: apply a checklist workflow to mcp security review work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_security_review_planner` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_security_review_planner",
  "arguments": {
    "completed": [
      "mcp security review schema validity",
      "mcp security review description clarity"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
