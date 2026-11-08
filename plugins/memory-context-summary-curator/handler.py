"""Handler for Context Summary Curator (memory-context-summary-curator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['context summary fact accuracy', 'context summary size budget fit', 'context summary staleness', 'context summary duplication', 'context summary source noted'], 'slug': 'memory-context-summary-curator', 'name': 'Context Summary Curator'}
def run(args):
    return run_engine(CONFIG, args or {})
