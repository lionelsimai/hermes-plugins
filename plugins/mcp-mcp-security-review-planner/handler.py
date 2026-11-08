"""Handler for Mcp Security Review Planner (mcp-mcp-security-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['mcp security review schema validity', 'mcp security review description clarity', 'mcp security review least privilege', 'mcp security review test coverage', 'mcp security review error behaviour'], 'slug': 'mcp-mcp-security-review-planner', 'name': 'Mcp Security Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
