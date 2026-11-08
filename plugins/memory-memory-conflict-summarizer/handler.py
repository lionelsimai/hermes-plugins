"""Handler for Memory Conflict Summarizer (memory-memory-conflict-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['memory conflict fact accuracy', 'memory conflict size budget fit', 'memory conflict staleness', 'memory conflict duplication', 'memory conflict source noted'], 'slug': 'memory-memory-conflict-summarizer', 'name': 'Memory Conflict Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
