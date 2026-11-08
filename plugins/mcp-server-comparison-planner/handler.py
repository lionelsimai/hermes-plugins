"""Handler for Server Comparison Planner (mcp-server-comparison-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['server comparison schema validity', 'server comparison description clarity', 'server comparison least privilege', 'server comparison test coverage', 'server comparison error behaviour'], 'slug': 'mcp-server-comparison-planner', 'name': 'Server Comparison Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
