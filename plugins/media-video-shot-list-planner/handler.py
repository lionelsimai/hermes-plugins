"""Handler for Video Shot List Planner (media-video-shot-list-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['video shot list brief clarity', 'video shot list format spec', 'video shot list rights and consent', 'video shot list quality gate', 'video shot list approval gate'], 'slug': 'media-video-shot-list-planner', 'name': 'Video Shot List Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
