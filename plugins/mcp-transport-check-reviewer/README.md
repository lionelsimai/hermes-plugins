# Transport Check Reviewer

Transport Check Reviewer for Hermes Agent: apply a analyze workflow to transport check work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_transport_check_reviewer` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_transport_check_reviewer",
  "arguments": {
    "counts": {
      "transport_check_schema_validity": 40,
      "transport_check_description_clarity": 25,
      "transport_check_least_privilege": 10,
      "transport_check_test_coverage": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
