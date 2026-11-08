"""Handler for Mcp Install Checklist Planner (mcp-mcp-install-checklist-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['mcp install checklist schema validity', 'mcp install checklist description clarity', 'mcp install checklist least privilege', 'mcp install checklist test coverage', 'mcp install checklist error behaviour'], 'slug': 'mcp-mcp-install-checklist-planner', 'name': 'Mcp Install Checklist Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
