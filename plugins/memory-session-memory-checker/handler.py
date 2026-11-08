"""Handler for Session Memory Checker (memory-session-memory-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['session memory fact accuracy', 'session memory size budget fit', 'session memory staleness', 'session memory duplication', 'session memory source noted'], 'slug': 'memory-session-memory-checker', 'name': 'Session Memory Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
