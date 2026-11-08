"""Handler for Video Shot List Drafter (media-video-shot-list-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['video shot list brief clarity', 'video shot list format spec', 'video shot list rights and consent', 'video shot list quality gate', 'video shot list approval gate'], 'slug': 'media-video-shot-list-drafter', 'name': 'Video Shot List Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
