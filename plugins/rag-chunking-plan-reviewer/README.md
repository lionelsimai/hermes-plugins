# Chunking Plan Reviewer

Chunking Plan Reviewer for Hermes Agent: apply a audit workflow to chunking plan work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_chunking_plan_reviewer` (kind: audit)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_chunking_plan_reviewer",
  "arguments": {
    "text": "This sample covers chunking plan source fidelity and chunking plan retrieval relevance in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
