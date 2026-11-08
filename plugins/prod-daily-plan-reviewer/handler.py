"""Handler for Daily Plan Reviewer (prod-daily-plan-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['daily plan priority clarity', 'daily plan time realism', 'daily plan next action named', 'daily plan review cadence', 'daily plan owner named'], 'slug': 'prod-daily-plan-reviewer', 'name': 'Daily Plan Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
