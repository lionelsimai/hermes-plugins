"""Handler for Habit Tracker Planner (prod-habit-tracker-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['habit tracker priority clarity', 'habit tracker time realism', 'habit tracker next action named', 'habit tracker review cadence', 'habit tracker owner named'], 'slug': 'prod-habit-tracker-planner', 'name': 'Habit Tracker Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
