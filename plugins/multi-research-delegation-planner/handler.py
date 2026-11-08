"""Handler for Research Delegation Planner (multi-research-delegation-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['research delegation scope clarity', 'research delegation independence of subtasks', 'research delegation merge criteria', 'research delegation context budget', 'research delegation verification step'], 'slug': 'multi-research-delegation-planner', 'name': 'Research Delegation Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
