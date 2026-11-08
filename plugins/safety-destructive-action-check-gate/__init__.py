"""Hermes plugin entry point for Destructive Action Check Gate.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="safety_destructive_action_check_gate", toolset="skills",
                      schema={"name": "safety_destructive_action_check_gate", "description": 'Destructive Action Check Gate for Hermes Agent: apply a score workflow to destructive action check work — covers risk identified, approval required and audit logged, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
