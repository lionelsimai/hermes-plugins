"""Handler for Tool Description Audit Drafter (mcp-tool-description-audit-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['tool description audit schema validity', 'tool description audit description clarity', 'tool description audit least privilege', 'tool description audit test coverage', 'tool description audit error behaviour'], 'slug': 'mcp-tool-description-audit-drafter', 'name': 'Tool Description Audit Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
