"""Handler for Archive Bundle Planner (files-archive-bundle-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['archive bundle format fit', 'archive bundle completeness', 'archive bundle naming consistency', 'archive bundle source fidelity', 'archive bundle output location'], 'slug': 'files-archive-bundle-planner', 'name': 'Archive Bundle Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
