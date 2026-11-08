"""Handler for Session Recall Planner (memory-session-recall-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['session recall fact accuracy', 'session recall size budget fit', 'session recall staleness', 'session recall duplication', 'session recall source noted'], 'slug': 'memory-session-recall-planner', 'name': 'Session Recall Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
