"""Handler for Review Delegation Reviewer (multi-review-delegation-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['review delegation scope clarity', 'review delegation independence of subtasks', 'review delegation merge criteria', 'review delegation context budget', 'review delegation verification step'], 'slug': 'multi-review-delegation-reviewer', 'name': 'Review Delegation Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
