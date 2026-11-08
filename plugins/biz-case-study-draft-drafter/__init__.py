"""Hermes plugin entry point for Case Study Draft Drafter.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="biz_case_study_draft_drafter", toolset="web",
                      schema={"name": "biz_case_study_draft_drafter", "description": 'Case Study Draft Drafter for Hermes Agent: apply a classify workflow to case study draft work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
