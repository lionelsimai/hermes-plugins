"""Handler for Tool Schema Draft Checker (mcp-tool-schema-draft-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['tool schema draft schema validity', 'tool schema draft description clarity', 'tool schema draft least privilege', 'tool schema draft test coverage', 'tool schema draft error behaviour'], 'slug': 'mcp-tool-schema-draft-checker', 'name': 'Tool Schema Draft Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
