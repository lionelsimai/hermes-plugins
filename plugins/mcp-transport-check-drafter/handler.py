"""Handler for Transport Check Drafter (mcp-transport-check-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['transport check schema validity', 'transport check description clarity', 'transport check least privilege', 'transport check test coverage', 'transport check error behaviour'], 'slug': 'mcp-transport-check-drafter', 'name': 'Transport Check Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
