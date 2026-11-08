"""Handler for Mcp Server Review Drafter (mcp-mcp-server-review-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['mcp server review schema validity', 'mcp server review description clarity', 'mcp server review least privilege', 'mcp server review test coverage', 'mcp server review error behaviour'], 'slug': 'mcp-mcp-server-review-drafter', 'name': 'Mcp Server Review Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
