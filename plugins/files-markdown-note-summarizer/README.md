# Markdown Note Summarizer

Markdown Note Summarizer for Hermes Agent: apply a classify workflow to markdown note work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_markdown_note_summarizer` (kind: classify)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_markdown_note_summarizer",
  "arguments": {
    "text": "Please review: this concerns markdown note format fit and markdown note naming consistency."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
