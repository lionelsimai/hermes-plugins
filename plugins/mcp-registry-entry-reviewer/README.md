# Registry Entry Reviewer

Registry Entry Reviewer for Hermes Agent: apply a score workflow to registry entry work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_registry_entry_reviewer` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_registry_entry_reviewer",
  "arguments": {
    "metrics": {
      "registry_entry_schema_validity": 80,
      "registry_entry_description_clarity": 65,
      "registry_entry_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
