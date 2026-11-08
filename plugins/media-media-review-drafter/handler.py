"""Handler for Media Review Drafter (media-media-review-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['media review brief clarity', 'media review format spec', 'media review rights and consent', 'media review quality gate', 'media review approval gate'], 'slug': 'media-media-review-drafter', 'name': 'Media Review Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
