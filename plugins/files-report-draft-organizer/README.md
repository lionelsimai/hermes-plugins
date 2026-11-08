# Report Draft Organizer

Report Draft Organizer for Hermes Agent: apply a analyze workflow to report draft work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_report_draft_organizer` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_report_draft_organizer",
  "arguments": {
    "counts": {
      "report_draft_format_fit": 40,
      "report_draft_completeness": 25,
      "report_draft_naming_consistency": 10,
      "report_draft_source_fidelity": 75
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
