"""Handler for Session Recall Checker (memory-session-recall-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['session recall fact accuracy', 'session recall size budget fit', 'session recall staleness', 'session recall duplication', 'session recall source noted'], 'slug': 'memory-session-recall-checker', 'name': 'Session Recall Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
