"""Handler for Mcp Security Review Checker (mcp-mcp-security-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['mcp security review schema validity', 'mcp security review description clarity', 'mcp security review least privilege', 'mcp security review test coverage', 'mcp security review error behaviour'], 'slug': 'mcp-mcp-security-review-checker', 'name': 'Mcp Security Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
