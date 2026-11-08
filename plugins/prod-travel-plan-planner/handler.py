"""Handler for Travel Plan Planner (prod-travel-plan-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['travel plan priority clarity', 'travel plan time realism', 'travel plan next action named', 'travel plan review cadence', 'travel plan owner named'], 'slug': 'prod-travel-plan-planner', 'name': 'Travel Plan Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
