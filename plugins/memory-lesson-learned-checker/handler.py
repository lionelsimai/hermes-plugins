"""Handler for Lesson Learned Checker (memory-lesson-learned-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['lesson learned fact accuracy', 'lesson learned size budget fit', 'lesson learned staleness', 'lesson learned duplication', 'lesson learned source noted'], 'slug': 'memory-lesson-learned-checker', 'name': 'Lesson Learned Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
