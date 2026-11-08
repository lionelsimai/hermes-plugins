"""Handler for Mcp Server Review Planner (mcp-mcp-server-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['mcp server review schema validity', 'mcp server review description clarity', 'mcp server review least privilege', 'mcp server review test coverage', 'mcp server review error behaviour'], 'slug': 'mcp-mcp-server-review-planner', 'name': 'Mcp Server Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
