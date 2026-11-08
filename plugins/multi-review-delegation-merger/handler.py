"""Handler for Review Delegation Merger (multi-review-delegation-merger). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['review delegation scope clarity', 'review delegation independence of subtasks', 'review delegation merge criteria', 'review delegation context budget', 'review delegation verification step'], 'slug': 'multi-review-delegation-merger', 'name': 'Review Delegation Merger'}
def run(args):
    return run_engine(CONFIG, args or {})
