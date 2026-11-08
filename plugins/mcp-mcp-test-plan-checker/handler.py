"""Handler for Mcp Test Plan Checker (mcp-mcp-test-plan-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['mcp test plan schema validity', 'mcp test plan description clarity', 'mcp test plan least privilege', 'mcp test plan test coverage', 'mcp test plan error behaviour'], 'slug': 'mcp-mcp-test-plan-checker', 'name': 'Mcp Test Plan Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
