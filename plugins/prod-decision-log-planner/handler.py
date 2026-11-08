"""Handler for Decision Log Planner (prod-decision-log-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['decision log priority clarity', 'decision log time realism', 'decision log next action named', 'decision log review cadence', 'decision log owner named'], 'slug': 'prod-decision-log-planner', 'name': 'Decision Log Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
