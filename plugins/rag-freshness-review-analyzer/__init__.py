"""Hermes plugin entry point for Freshness Review Analyzer.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="rag_freshness_review_analyzer", toolset="memory",
                      schema={"name": "rag_freshness_review_analyzer", "description": 'Freshness Review Analyzer for Hermes Agent: apply a template workflow to freshness review work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
