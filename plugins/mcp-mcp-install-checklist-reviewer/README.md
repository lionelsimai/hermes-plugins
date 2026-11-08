# Mcp Install Checklist Reviewer

Mcp Install Checklist Reviewer for Hermes Agent: apply a audit workflow to mcp install checklist work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_install_checklist_reviewer` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_install_checklist_reviewer",
  "arguments": {
    "text": "This sample covers mcp install checklist schema validity and mcp install checklist description clarity in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
