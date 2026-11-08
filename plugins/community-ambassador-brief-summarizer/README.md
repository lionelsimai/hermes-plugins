# Ambassador Brief Summarizer

Ambassador Brief Summarizer for Hermes Agent: apply a checklist workflow to ambassador brief work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_ambassador_brief_summarizer` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_ambassador_brief_summarizer",
  "arguments": {
    "completed": [
      "ambassador brief member fit",
      "ambassador brief tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
