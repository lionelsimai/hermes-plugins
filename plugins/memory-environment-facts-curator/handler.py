"""Handler for Environment Facts Curator (memory-environment-facts-curator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['environment facts fact accuracy', 'environment facts size budget fit', 'environment facts staleness', 'environment facts duplication', 'environment facts source noted'], 'slug': 'memory-environment-facts-curator', 'name': 'Environment Facts Curator'}
def run(args):
    return run_engine(CONFIG, args or {})
