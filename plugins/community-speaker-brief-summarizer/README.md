# Speaker Brief Summarizer

Speaker Brief Summarizer for Hermes Agent: apply a audit workflow to speaker brief work — covers member fit, tone fit and follow up named, using supplied facts only.

- Category: Community Ops
- Tool: `community_speaker_brief_summarizer` (kind: audit)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "community_speaker_brief_summarizer",
  "arguments": {
    "text": "This sample covers speaker brief member fit and speaker brief tone fit in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
