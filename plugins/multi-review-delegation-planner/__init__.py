"""Hermes plugin entry point for Review Delegation Planner.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="multi_review_delegation_planner", toolset="delegation",
                      schema={"name": "multi_review_delegation_planner", "description": 'Review Delegation Planner for Hermes Agent: apply a score workflow to review delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
