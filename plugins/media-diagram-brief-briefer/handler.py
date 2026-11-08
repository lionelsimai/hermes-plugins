"""Handler for Diagram Brief Briefer (media-diagram-brief-briefer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['diagram brief brief clarity', 'diagram brief format spec', 'diagram brief rights and consent', 'diagram brief quality gate', 'diagram brief approval gate'], 'slug': 'media-diagram-brief-briefer', 'name': 'Diagram Brief Briefer'}
def run(args):
    return run_engine(CONFIG, args or {})
