"""Handler for Learning Plan Triage Tool (prod-learning-plan-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['learning plan priority clarity', 'learning plan time realism', 'learning plan next action named', 'learning plan review cadence', 'learning plan owner named'], 'slug': 'prod-learning-plan-triage-tool', 'name': 'Learning Plan Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
