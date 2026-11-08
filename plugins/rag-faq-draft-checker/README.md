# Faq Draft Checker

Faq Draft Checker for Hermes Agent: apply a audit workflow to faq draft work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_faq_draft_checker` (kind: audit)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_faq_draft_checker",
  "arguments": {
    "text": "This sample covers faq draft source fidelity and faq draft retrieval relevance in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
