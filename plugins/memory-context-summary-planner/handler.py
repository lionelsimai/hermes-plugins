"""Handler for Context Summary Planner (memory-context-summary-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['context summary fact accuracy', 'context summary size budget fit', 'context summary staleness', 'context summary duplication', 'context summary source noted'], 'slug': 'memory-context-summary-planner', 'name': 'Context Summary Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
