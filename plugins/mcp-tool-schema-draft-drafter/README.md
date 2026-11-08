# Tool Schema Draft Drafter

Tool Schema Draft Drafter for Hermes Agent: apply a checklist workflow to tool schema draft work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_tool_schema_draft_drafter` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_tool_schema_draft_drafter",
  "arguments": {
    "completed": [
      "tool schema draft schema validity",
      "tool schema draft description clarity"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
