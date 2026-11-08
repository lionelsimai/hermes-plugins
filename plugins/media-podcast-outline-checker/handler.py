"""Handler for Podcast Outline Checker (media-podcast-outline-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['podcast outline brief clarity', 'podcast outline format spec', 'podcast outline rights and consent', 'podcast outline quality gate', 'podcast outline approval gate'], 'slug': 'media-podcast-outline-checker', 'name': 'Podcast Outline Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
