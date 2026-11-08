# Document Outline Summarizer

Document Outline Summarizer for Hermes Agent: apply a analyze workflow to document outline work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_document_outline_summarizer` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_document_outline_summarizer",
  "arguments": {
    "counts": {
      "document_outline_format_fit": 40,
      "document_outline_completeness": 25,
      "document_outline_naming_consistency": 10,
      "document_outline_source_fidelity": 75
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
