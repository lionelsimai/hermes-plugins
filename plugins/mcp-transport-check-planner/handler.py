"""Handler for Transport Check Planner (mcp-transport-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['transport check schema validity', 'transport check description clarity', 'transport check least privilege', 'transport check test coverage', 'transport check error behaviour'], 'slug': 'mcp-transport-check-planner', 'name': 'Transport Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
