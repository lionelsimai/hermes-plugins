# Document Outline Checker

Document Outline Checker for Hermes Agent: apply a classify workflow to document outline work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_document_outline_checker` (kind: classify)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_document_outline_checker",
  "arguments": {
    "text": "Please review: this concerns document outline format fit and document outline naming consistency."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
