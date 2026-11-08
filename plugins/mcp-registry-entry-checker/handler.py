"""Handler for Registry Entry Checker (mcp-registry-entry-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['registry entry schema validity', 'registry entry description clarity', 'registry entry least privilege', 'registry entry test coverage', 'registry entry error behaviour'], 'slug': 'mcp-registry-entry-checker', 'name': 'Registry Entry Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
