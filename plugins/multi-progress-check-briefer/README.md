# Progress Check Briefer

Progress Check Briefer for Hermes Agent: apply a audit workflow to progress check work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_progress_check_briefer` (kind: audit)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_progress_check_briefer",
  "arguments": {
    "text": "This sample covers progress check scope clarity and progress check independence of subtasks in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
