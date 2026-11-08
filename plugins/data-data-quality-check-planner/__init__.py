"""Hermes plugin entry point for Data Quality Check Planner.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="data_data_quality_check_planner", toolset="file",
                      schema={"name": "data_data_quality_check_planner", "description": 'Data Quality Check Planner for Hermes Agent: apply a classify workflow to data quality check work — covers data completeness, column consistency and format fit, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
