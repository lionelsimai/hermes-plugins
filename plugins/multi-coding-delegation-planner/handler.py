"""Handler for Coding Delegation Planner (multi-coding-delegation-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['coding delegation scope clarity', 'coding delegation independence of subtasks', 'coding delegation merge criteria', 'coding delegation context budget', 'coding delegation verification step'], 'slug': 'multi-coding-delegation-planner', 'name': 'Coding Delegation Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
