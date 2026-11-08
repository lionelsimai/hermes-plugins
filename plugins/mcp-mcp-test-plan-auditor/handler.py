"""Handler for Mcp Test Plan Auditor (mcp-mcp-test-plan-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['mcp test plan schema validity', 'mcp test plan description clarity', 'mcp test plan least privilege', 'mcp test plan test coverage', 'mcp test plan error behaviour'], 'slug': 'mcp-mcp-test-plan-auditor', 'name': 'Mcp Test Plan Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
