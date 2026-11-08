# Tool Description Audit Reviewer

Tool Description Audit Reviewer for Hermes Agent: apply a template workflow to tool description audit work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_tool_description_audit_reviewer` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_tool_description_audit_reviewer",
  "arguments": {
    "facts": {
      "tool_description_audit_schema_validity": "Sample supplied fact",
      "tool_description_audit_description_clarity": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
