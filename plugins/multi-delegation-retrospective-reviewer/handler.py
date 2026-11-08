"""Handler for Delegation Retrospective Reviewer (multi-delegation-retrospective-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['delegation retrospective scope clarity', 'delegation retrospective independence of subtasks', 'delegation retrospective merge criteria', 'delegation retrospective context budget', 'delegation retrospective verification step'], 'slug': 'multi-delegation-retrospective-reviewer', 'name': 'Delegation Retrospective Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
