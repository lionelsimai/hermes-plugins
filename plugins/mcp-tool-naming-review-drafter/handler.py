"""Handler for Tool Naming Review Drafter (mcp-tool-naming-review-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['tool naming review schema validity', 'tool naming review description clarity', 'tool naming review least privilege', 'tool naming review test coverage', 'tool naming review error behaviour'], 'slug': 'mcp-tool-naming-review-drafter', 'name': 'Tool Naming Review Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
