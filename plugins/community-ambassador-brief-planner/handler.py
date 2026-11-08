"""Handler for Ambassador Brief Planner (community-ambassador-brief-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['ambassador brief member fit', 'ambassador brief tone fit', 'ambassador brief approval gate', 'ambassador brief safety check', 'ambassador brief follow up named'], 'slug': 'community-ambassador-brief-planner', 'name': 'Ambassador Brief Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
