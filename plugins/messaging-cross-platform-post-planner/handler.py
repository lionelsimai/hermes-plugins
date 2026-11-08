"""Handler for Cross Platform Post Planner (messaging-cross-platform-post-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['cross platform post audience fit', 'cross platform post tone fit', 'cross platform post length fit', 'cross platform post approval gate', 'cross platform post platform fit'], 'slug': 'messaging-cross-platform-post-planner', 'name': 'Cross Platform Post Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
