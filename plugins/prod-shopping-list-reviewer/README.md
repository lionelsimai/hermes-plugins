# Shopping List Reviewer

Shopping List Reviewer for Hermes Agent: apply a checklist workflow to shopping list work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_shopping_list_reviewer` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_shopping_list_reviewer",
  "arguments": {
    "completed": [
      "shopping list priority clarity",
      "shopping list time realism"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
