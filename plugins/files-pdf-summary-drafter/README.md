# Pdf Summary Drafter

Pdf Summary Drafter for Hermes Agent: apply a score workflow to pdf summary work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_pdf_summary_drafter` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_pdf_summary_drafter",
  "arguments": {
    "metrics": {
      "pdf_summary_format_fit": 80,
      "pdf_summary_completeness": 65,
      "pdf_summary_naming_consistency": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
