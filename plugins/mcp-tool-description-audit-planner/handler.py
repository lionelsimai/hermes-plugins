"""Handler for Tool Description Audit Planner (mcp-tool-description-audit-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['tool description audit schema validity', 'tool description audit description clarity', 'tool description audit least privilege', 'tool description audit test coverage', 'tool description audit error behaviour'], 'slug': 'mcp-tool-description-audit-planner', 'name': 'Tool Description Audit Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
