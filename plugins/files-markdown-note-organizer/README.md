# Markdown Note Organizer

Markdown Note Organizer for Hermes Agent: apply a analyze workflow to markdown note work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_markdown_note_organizer` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_markdown_note_organizer",
  "arguments": {
    "counts": {
      "markdown_note_format_fit": 40,
      "markdown_note_completeness": 25,
      "markdown_note_naming_consistency": 10,
      "markdown_note_source_fidelity": 75
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
