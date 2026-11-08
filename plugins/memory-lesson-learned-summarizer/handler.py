"""Handler for Lesson Learned Summarizer (memory-lesson-learned-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['lesson learned fact accuracy', 'lesson learned size budget fit', 'lesson learned staleness', 'lesson learned duplication', 'lesson learned source noted'], 'slug': 'memory-lesson-learned-summarizer', 'name': 'Lesson Learned Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
