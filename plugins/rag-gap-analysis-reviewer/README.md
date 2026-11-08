# Gap Analysis Reviewer

Gap Analysis Reviewer for Hermes Agent: apply a audit workflow to gap analysis work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_gap_analysis_reviewer` (kind: audit)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_gap_analysis_reviewer",
  "arguments": {
    "text": "This sample covers gap analysis source fidelity and gap analysis retrieval relevance in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
