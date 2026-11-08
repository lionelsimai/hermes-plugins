"""Hermes plugin entry point for Price Research Tracker.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="web_price_research_tracker", toolset="web",
                      schema={"name": "web_price_research_tracker", "description": 'Price Research Tracker for Hermes Agent: apply a plan workflow to price research work — covers source quality, recency and scope fit, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
