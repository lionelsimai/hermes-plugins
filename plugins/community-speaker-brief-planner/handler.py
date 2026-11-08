"""Handler for Speaker Brief Planner (community-speaker-brief-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['speaker brief member fit', 'speaker brief tone fit', 'speaker brief approval gate', 'speaker brief safety check', 'speaker brief follow up named'], 'slug': 'community-speaker-brief-planner', 'name': 'Speaker Brief Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
