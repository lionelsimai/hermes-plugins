"""Handler for Registry Entry Reviewer (mcp-registry-entry-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['registry entry schema validity', 'registry entry description clarity', 'registry entry least privilege', 'registry entry test coverage', 'registry entry error behaviour'], 'slug': 'mcp-registry-entry-reviewer', 'name': 'Registry Entry Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
