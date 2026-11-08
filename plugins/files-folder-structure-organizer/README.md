# Folder Structure Organizer

Folder Structure Organizer for Hermes Agent: apply a classify workflow to folder structure work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_folder_structure_organizer` (kind: classify)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_folder_structure_organizer",
  "arguments": {
    "text": "Please review: this concerns folder structure format fit and folder structure naming consistency."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
