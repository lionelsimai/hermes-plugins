# Changelog

## v1.0.0 — 9 Nov 2026

- 1,000 plugins across 20 categories for Hermes Agent (Nous Research).
- Each plugin ships the verified Hermes plugin format (plugin.yaml +
  __init__.py with register(ctx)/ctx.register_tool), a Hermes SKILL.md,
  and the collection-standard plugin.json + README + handler.
- Shared MCP server + REST server (stdlib Python only), registry-driven.
- Extraction-based design: official Hermes repo/docs, bundled-skills
  taxonomy and leading community collections — see SOURCES.md.
- Guardrails in code on every result: no fabrication, draft-only,
  human approval, no auto-send, no credential handling.
