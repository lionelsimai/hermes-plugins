"""Hermes plugin entry point for Environment Facts Summarizer.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="memory_environment_facts_summarizer", toolset="memory",
                      schema={"name": "memory_environment_facts_summarizer", "description": 'Environment Facts Summarizer for Hermes Agent: apply a prioritize workflow to environment facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
