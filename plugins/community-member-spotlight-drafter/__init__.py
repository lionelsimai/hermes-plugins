"""Hermes plugin entry point for Member Spotlight Drafter.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="community_member_spotlight_drafter", toolset="messaging",
                      schema={"name": "community_member_spotlight_drafter", "description": 'Member Spotlight Drafter for Hermes Agent: apply a template workflow to member spotlight work — covers member fit, tone fit and follow up named, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
