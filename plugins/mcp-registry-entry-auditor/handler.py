"""Handler for Registry Entry Auditor (mcp-registry-entry-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['registry entry schema validity', 'registry entry description clarity', 'registry entry least privilege', 'registry entry test coverage', 'registry entry error behaviour'], 'slug': 'mcp-registry-entry-auditor', 'name': 'Registry Entry Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
