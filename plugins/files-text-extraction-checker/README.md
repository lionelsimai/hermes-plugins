# Text Extraction Checker

Text Extraction Checker for Hermes Agent: apply a analyze workflow to text extraction work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_text_extraction_checker` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_text_extraction_checker",
  "arguments": {
    "counts": {
      "text_extraction_format_fit": 40,
      "text_extraction_completeness": 25,
      "text_extraction_naming_consistency": 10,
      "text_extraction_source_fidelity": 75
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
