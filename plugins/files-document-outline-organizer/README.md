# Document Outline Organizer

Document Outline Organizer for Hermes Agent: apply a template workflow to document outline work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_document_outline_organizer` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_document_outline_organizer",
  "arguments": {
    "facts": {
      "document_outline_format_fit": "Sample supplied fact",
      "document_outline_completeness": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
