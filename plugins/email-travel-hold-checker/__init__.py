"""Hermes plugin entry point for Travel Hold Checker.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="email_travel_hold_checker", toolset="messaging",
                      schema={"name": "email_travel_hold_checker", "description": 'Travel Hold Checker for Hermes Agent: apply a template workflow to travel hold work — covers priority accuracy, tone fit and next step clarity, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
