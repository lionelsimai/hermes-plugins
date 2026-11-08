"""Handler for Thumbnail Plan Planner (media-thumbnail-plan-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['thumbnail plan brief clarity', 'thumbnail plan format spec', 'thumbnail plan rights and consent', 'thumbnail plan quality gate', 'thumbnail plan approval gate'], 'slug': 'media-thumbnail-plan-planner', 'name': 'Thumbnail Plan Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
