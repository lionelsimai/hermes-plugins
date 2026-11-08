# Contributing

Issues and pull requests welcome. The bar:

- One plugin per folder under `plugins/<slug>/` with all six files:
  `plugin.json`, `plugin.yaml`, `__init__.py`, `SKILL.md`, `README.md`,
  `handler.py`.
- Keep the guardrails intact (no fabrication, draft-only, human
  approval, no auto-send, no credential handling).
- Keep handlers deterministic and stdlib-only; add the plugin to the
  generator data so `catalog.json` stays reproducible, and make sure
  `python3 tests/test_suite.py` passes.
- Fictional sample data only — no real people, clients or metrics.
