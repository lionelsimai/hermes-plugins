"""Handler for Mcp Security Review Drafter (mcp-mcp-security-review-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['mcp security review schema validity', 'mcp security review description clarity', 'mcp security review least privilege', 'mcp security review test coverage', 'mcp security review error behaviour'], 'slug': 'mcp-mcp-security-review-drafter', 'name': 'Mcp Security Review Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
