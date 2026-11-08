# Pdf Summary Organizer

Pdf Summary Organizer for Hermes Agent: apply a audit workflow to pdf summary work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_pdf_summary_organizer` (kind: audit)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_pdf_summary_organizer",
  "arguments": {
    "text": "This sample covers pdf summary format fit and pdf summary completeness in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
