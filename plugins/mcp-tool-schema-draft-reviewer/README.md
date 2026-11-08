# Tool Schema Draft Reviewer

Tool Schema Draft Reviewer for Hermes Agent: apply a score workflow to tool schema draft work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_tool_schema_draft_reviewer` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_tool_schema_draft_reviewer",
  "arguments": {
    "metrics": {
      "tool_schema_draft_schema_validity": 80,
      "tool_schema_draft_description_clarity": 65,
      "tool_schema_draft_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
