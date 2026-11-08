"""Handler for Tool Naming Review Checker (mcp-tool-naming-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['tool naming review schema validity', 'tool naming review description clarity', 'tool naming review least privilege', 'tool naming review test coverage', 'tool naming review error behaviour'], 'slug': 'mcp-tool-naming-review-checker', 'name': 'Tool Naming Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
