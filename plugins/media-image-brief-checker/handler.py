"""Handler for Image Brief Checker (media-image-brief-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['image brief brief clarity', 'image brief format spec', 'image brief rights and consent', 'image brief quality gate', 'image brief approval gate'], 'slug': 'media-image-brief-checker', 'name': 'Image Brief Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
