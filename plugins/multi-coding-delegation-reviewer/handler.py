"""Handler for Coding Delegation Reviewer (multi-coding-delegation-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['coding delegation scope clarity', 'coding delegation independence of subtasks', 'coding delegation merge criteria', 'coding delegation context budget', 'coding delegation verification step'], 'slug': 'multi-coding-delegation-reviewer', 'name': 'Coding Delegation Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
