"""Handler for Podcast Outline Reviewer (media-podcast-outline-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['podcast outline brief clarity', 'podcast outline format spec', 'podcast outline rights and consent', 'podcast outline quality gate', 'podcast outline approval gate'], 'slug': 'media-podcast-outline-reviewer', 'name': 'Podcast Outline Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
