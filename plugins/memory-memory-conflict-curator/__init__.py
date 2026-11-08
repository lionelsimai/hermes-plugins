"""Hermes plugin entry point for Memory Conflict Curator.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="memory_memory_conflict_curator", toolset="memory",
                      schema={"name": "memory_memory_conflict_curator", "description": 'Memory Conflict Curator for Hermes Agent: apply a classify workflow to memory conflict work — covers fact accuracy, size budget fit and source noted, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
