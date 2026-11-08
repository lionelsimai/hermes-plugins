# Report Draft Checker

Report Draft Checker for Hermes Agent: apply a audit workflow to report draft work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_report_draft_checker` (kind: audit)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_report_draft_checker",
  "arguments": {
    "text": "This sample covers report draft format fit and report draft completeness in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
