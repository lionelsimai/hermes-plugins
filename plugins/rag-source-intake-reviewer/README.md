# Source Intake Reviewer

Source Intake Reviewer for Hermes Agent: apply a score workflow to source intake work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_source_intake_reviewer` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_source_intake_reviewer",
  "arguments": {
    "metrics": {
      "source_intake_source_fidelity": 80,
      "source_intake_retrieval_relevance": 65,
      "source_intake_citation_coverage": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
