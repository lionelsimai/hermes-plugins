"""Hermes plugin entry point for Lead List Check Scorer.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="biz_lead_list_check_scorer", toolset="web",
                      schema={"name": "biz_lead_list_check_scorer", "description": 'Lead List Check Scorer for Hermes Agent: apply a classify workflow to lead list check work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
