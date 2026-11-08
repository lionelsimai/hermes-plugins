# Folder Structure Planner

Folder Structure Planner for Hermes Agent: apply a score workflow to folder structure work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_folder_structure_planner` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_folder_structure_planner",
  "arguments": {
    "metrics": {
      "folder_structure_format_fit": 80,
      "folder_structure_completeness": 65,
      "folder_structure_naming_consistency": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
