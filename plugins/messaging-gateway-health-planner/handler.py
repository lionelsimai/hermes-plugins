"""Handler for Gateway Health Planner (messaging-gateway-health-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['gateway health audience fit', 'gateway health tone fit', 'gateway health length fit', 'gateway health approval gate', 'gateway health platform fit'], 'slug': 'messaging-gateway-health-planner', 'name': 'Gateway Health Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
