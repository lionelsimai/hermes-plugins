"""Hermes plugin entry point for Login Flow Check Sequencer.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="browser_login_flow_check_sequencer", toolset="browser",
                      schema={"name": "browser_login_flow_check_sequencer", "description": 'Login Flow Check Sequencer for Hermes Agent: apply a classify workflow to login flow check work — covers step clarity, fallback step and completion proof, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
