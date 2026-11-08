# Tool Permission Review Reviewer

Tool Permission Review Reviewer for Hermes Agent: apply a classify workflow to tool permission review work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_tool_permission_review_reviewer` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_tool_permission_review_reviewer",
  "arguments": {
    "text": "Please review: this concerns tool permission review risk identified and tool permission review least privilege."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
