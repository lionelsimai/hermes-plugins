# Tool Schema Draft Checker

Tool Schema Draft Checker for Hermes Agent: apply a classify workflow to tool schema draft work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_tool_schema_draft_checker` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_tool_schema_draft_checker",
  "arguments": {
    "text": "Please review: this concerns tool schema draft schema validity and tool schema draft least privilege."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
