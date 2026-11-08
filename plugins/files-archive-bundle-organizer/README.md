# Archive Bundle Organizer

Archive Bundle Organizer for Hermes Agent: apply a score workflow to archive bundle work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_archive_bundle_organizer` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_archive_bundle_organizer",
  "arguments": {
    "metrics": {
      "archive_bundle_format_fit": 80,
      "archive_bundle_completeness": 65,
      "archive_bundle_naming_consistency": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
