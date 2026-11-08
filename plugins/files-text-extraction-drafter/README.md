# Text Extraction Drafter

Text Extraction Drafter for Hermes Agent: apply a classify workflow to text extraction work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_text_extraction_drafter` (kind: classify)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_text_extraction_drafter",
  "arguments": {
    "text": "Please review: this concerns text extraction format fit and text extraction naming consistency."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
