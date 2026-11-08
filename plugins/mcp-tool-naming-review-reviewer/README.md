# Tool Naming Review Reviewer

Tool Naming Review Reviewer for Hermes Agent: apply a checklist workflow to tool naming review work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_tool_naming_review_reviewer` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_tool_naming_review_reviewer",
  "arguments": {
    "completed": [
      "tool naming review schema validity",
      "tool naming review description clarity"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
