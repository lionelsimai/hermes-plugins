"""Handler for Memory Conflict Planner (memory-memory-conflict-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['memory conflict fact accuracy', 'memory conflict size budget fit', 'memory conflict staleness', 'memory conflict duplication', 'memory conflict source noted'], 'slug': 'memory-memory-conflict-planner', 'name': 'Memory Conflict Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
