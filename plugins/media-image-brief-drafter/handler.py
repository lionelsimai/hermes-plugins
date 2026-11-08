"""Handler for Image Brief Drafter (media-image-brief-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['image brief brief clarity', 'image brief format spec', 'image brief rights and consent', 'image brief quality gate', 'image brief approval gate'], 'slug': 'media-image-brief-drafter', 'name': 'Image Brief Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
