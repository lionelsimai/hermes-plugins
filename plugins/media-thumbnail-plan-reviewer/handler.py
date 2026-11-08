"""Handler for Thumbnail Plan Reviewer (media-thumbnail-plan-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['thumbnail plan brief clarity', 'thumbnail plan format spec', 'thumbnail plan rights and consent', 'thumbnail plan quality gate', 'thumbnail plan approval gate'], 'slug': 'media-thumbnail-plan-reviewer', 'name': 'Thumbnail Plan Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
