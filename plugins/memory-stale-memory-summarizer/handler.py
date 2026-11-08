"""Handler for Stale Memory Summarizer (memory-stale-memory-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['stale memory fact accuracy', 'stale memory size budget fit', 'stale memory staleness', 'stale memory duplication', 'stale memory source noted'], 'slug': 'memory-stale-memory-summarizer', 'name': 'Stale Memory Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
