"""Handler for Tool Schema Draft Drafter (mcp-tool-schema-draft-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['tool schema draft schema validity', 'tool schema draft description clarity', 'tool schema draft least privilege', 'tool schema draft test coverage', 'tool schema draft error behaviour'], 'slug': 'mcp-tool-schema-draft-drafter', 'name': 'Tool Schema Draft Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
