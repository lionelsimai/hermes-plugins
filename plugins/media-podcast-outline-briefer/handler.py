"""Handler for Podcast Outline Briefer (media-podcast-outline-briefer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['podcast outline brief clarity', 'podcast outline format spec', 'podcast outline rights and consent', 'podcast outline quality gate', 'podcast outline approval gate'], 'slug': 'media-podcast-outline-briefer', 'name': 'Podcast Outline Briefer'}
def run(args):
    return run_engine(CONFIG, args or {})
