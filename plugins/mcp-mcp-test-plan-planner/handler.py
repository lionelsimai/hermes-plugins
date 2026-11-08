"""Handler for Mcp Test Plan Planner (mcp-mcp-test-plan-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['mcp test plan schema validity', 'mcp test plan description clarity', 'mcp test plan least privilege', 'mcp test plan test coverage', 'mcp test plan error behaviour'], 'slug': 'mcp-mcp-test-plan-planner', 'name': 'Mcp Test Plan Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
